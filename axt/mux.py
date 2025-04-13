import argparse
import base64
import textwrap

def format_py(payload):
    return f'payload = "{payload}"'

def format_c(payload):
    return 'char payload[] = "' + ''.join([f"\\x{ord(c):02x}" for c in payload]) + '";'

def format_ps1(payload):
    encoded = base64.b64encode(payload.encode('utf-16le')).decode()
    return f'powershell -EncodedCommand {encoded}'

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx axt --type mux",
        description="Format dan encode payload (C, Python, PowerShell)",
        epilog="Contoh: python ctrlx.py axt --type mux --input \"bash ...\" --format py --save"
    )

    parser.add_argument("--input", required=True, help="Payload string untuk diformat")
    parser.add_argument("--format", choices=["py", "c", "ps1"], required=True, help="Format output: py, c, atau ps1")

    args = parser.parse_args(raw_args)
    input_payload = args.input.strip()

    if args.format == "py":
        return format_py(input_payload)
    elif args.format == "c":
        return format_c(input_payload)
    elif args.format == "ps1":
        return format_ps1(input_payload)
    else:
        return "[!] Format tidak dikenali."

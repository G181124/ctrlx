import argparse
import base64
import textwrap

def to_c_format(shellcode):
    return f'unsigned char shellcode[] = \n"{shellcode}";'

def to_python_format(shellcode):
    return f'shellcode = b"{shellcode}"'

def to_ps1_format(shellcode):
    raw_bytes = bytes(shellcode.encode().decode('unicode_escape'), 'latin1')
    encoded = base64.b64encode(raw_bytes).decode()
    return f'[Byte[]]$buf = [System.Convert]::FromBase64String("{encoded}")'

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx zkf --type sch",
        description="Format shellcode into C, Python, or PowerShell style",
        epilog="Contoh: --input \"\\x90\\x90\\xcc\" --format c"
    )

    parser.add_argument("--input", required=True, help="Shellcode dalam bentuk string escaped (misal: \\x90\\xcc)")
    parser.add_argument("--format", choices=["c", "py", "ps1"], required=True, help="Target output format")

    args = parser.parse_args(raw_args)

    if args.format == "c":
        return to_c_format(args.input)
    elif args.format == "py":
        return to_python_format(args.input)
    elif args.format == "ps1":
        return to_ps1_format(args.input)
    else:
        return "[!] Format tidak dikenali"

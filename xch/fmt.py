import argparse
import base64

def format_py(s):
    return f'shellcode = b"{s}"'

def format_c(s):
    return f'unsigned char shellcode[] = \n"{s}";'

def format_ps1(s):
    raw_bytes = bytes(s.encode().decode('unicode_escape'), 'latin1')
    encoded = base64.b64encode(raw_bytes).decode()
    return f'[Byte[]]$buf = [System.Convert]::FromBase64String("{encoded}")'

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx xch --type fmt",
        description="Format shellcode ke Python, C, PowerShell, atau raw",
        epilog="Contoh: --input \"\\x90\\x90\\xcc\" --format py"
    )

    parser.add_argument("--input", required=True, help="Shellcode atau string escaped")
    parser.add_argument("--format", choices=["py", "c", "ps1", "raw"], required=True, help="Format output")

    args = parser.parse_args(raw_args)

    if args.format == "py":
        return format_py(args.input)
    elif args.format == "c":
        return format_c(args.input)
    elif args.format == "ps1":
        return format_ps1(args.input)
    elif args.format == "raw":
        return args.input
    else:
        return "[✖] Format tidak dikenali"

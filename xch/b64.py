import argparse
import base64

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx xch --type b64",
        description="Base64 encoder untuk payload/shellcode",
        epilog="Contoh: --input \"whoami\""
    )

    parser.add_argument("--input", required=True, help="Teks atau payload yang ingin di-encode")

    args = parser.parse_args(raw_args)
    encoded = base64.b64encode(args.input.encode()).decode()

    return f"[📤] Base64 Encoded:\n{encoded}"

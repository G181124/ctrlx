import argparse

def hex_encode(text):
    return ''.join(f'\\x{ord(c):02x}' for c in text)

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx xch --type hx0",
        description="Hex encoder untuk shellcode atau payload",
        epilog="Contoh: --input \"whoami\""
    )

    parser.add_argument("--input", required=True, help="Teks yang ingin diubah menjadi hex escaped")

    args = parser.parse_args(raw_args)
    encoded = hex_encode(args.input)

    return f"[📤] Hex Encoded:\n{encoded}"

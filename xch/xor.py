import argparse

def xor_encode(text, key):
    return ''.join(f"\\x{ord(c) ^ ord(key):02x}" for c in text)

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx xch --type xor",
        description="XOR encoder untuk obfuscate payload sederhana",
        epilog="Contoh: --input \"whoami\" --key x"
    )

    parser.add_argument("--input", required=True, help="Payload atau teks yang ingin diencode")
    parser.add_argument("--key", required=True, help="1 karakter untuk XOR key (misal: x)")

    args = parser.parse_args(raw_args)

    if len(args.key) != 1:
        return "[✖] Kunci XOR harus 1 karakter saja."

    encoded = xor_encode(args.input, args.key)
    return f"[📤] XOR Encoded:\n{encoded}"

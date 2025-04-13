import argparse
import os
import random
import string

def random_name(prefix="", length=6, extension=""):
    name = prefix + ''.join(random.choices(string.ascii_lowercase, k=length))
    if extension:
        name += extension
    return name

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx rda --type vlt",
        description="Rename file menjadi nama sistem yang tidak mencolok (obfuscator)",
        epilog="Contoh: python ctrlx.py rda --type vlt --input payload.sh --save"
    )

    parser.add_argument("--input", required=True, help="Nama file yang akan disamarkan (tidak akan diubah fisik)")
    parser.add_argument("--prefix", default=".", help="Awalan nama (default: titik)")
    parser.add_argument("--length", type=int, default=6, help="Panjang nama acak setelah prefix")

    args = parser.parse_args(raw_args)

    original = args.input
    ext = os.path.splitext(original)[1]
    disguised = random_name(prefix=args.prefix, length=args.length, extension=ext)

    return f"[📤] Nama asli: {original}\n[🎭] Nama disamarkan: {disguised}"

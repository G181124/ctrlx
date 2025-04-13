import argparse
import random
import textwrap

def chunk_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx xch --type snk",
        description="Byte chunker dan shuffler untuk payload/shellcode",
        epilog="Contoh: --input \"bash\" --chunk 2  atau  --shuffle"
    )

    parser.add_argument("--input", required=True, help="Teks atau payload")
    parser.add_argument("--chunk", type=int, help="Panjang tiap potongan (misal 4)")
    parser.add_argument("--shuffle", action="store_true", help="Acak urutan byte")

    args = parser.parse_args(raw_args)

    data = list(args.input)

    if args.chunk:
        chunks = chunk_string(args.input, args.chunk)
        return "[📤] Chunked Output:\n" + "\n".join(chunks)

    if args.shuffle:
        random.shuffle(data)
        return "[📤] Shuffled Output:\n" + ''.join(data)

    return "[✖] Gunakan --chunk N atau --shuffle untuk melanjutkan."

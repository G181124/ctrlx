import argparse
import itertools

def generate_words(chars, min_len, max_len):
    words = []
    for l in range(min_len, max_len + 1):
        for combo in itertools.product(chars, repeat=l):
            words.append(''.join(combo))
    return '\n'.join(words)

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx qrn --type crh",
        description="Generate custom character-based wordlist (crunch-style)",
        epilog="Contoh: python ctrlx.py qrn --type crh --chars abc123 --min 3 --max 4 --save"
    )

    parser.add_argument("--chars", required=True, help="Karakter yang digunakan dalam kombinasi")
    parser.add_argument("--min", type=int, default=3, help="Panjang minimum kombinasi (default: 3)")
    parser.add_argument("--max", type=int, default=4, help="Panjang maksimum kombinasi (default: 4)")

    args = parser.parse_args(raw_args)
    return generate_words(args.chars, args.min, args.max)

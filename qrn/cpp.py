import argparse

def generate_profile_wordlist(name, birth, pet, hobby):
    base = [name, birth, pet, hobby]
    base = [x for x in base if x]
    combos = set()
    for word in base:
        combos.update({word, word.lower(), word.upper(), word.capitalize(), word + "123", word + "!", word[::-1]})
    return '\n'.join(sorted(combos))

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx qrn --type cpp",
        description="Generate wordlist based on user profile (CUPP-style)",
        epilog="Contoh: python ctrlx.py qrn --type cpp --name adi --birth 1995 --pet blacky --hobby coding --save"
    )

    parser.add_argument("--name", help="Nama target")
    parser.add_argument("--birth", help="Tahun lahir atau tanggal khusus")
    parser.add_argument("--pet", help="Nama hewan peliharaan")
    parser.add_argument("--hobby", help="Hobi target")

    args = parser.parse_args(raw_args)
    return generate_profile_wordlist(args.name, args.birth, args.pet, args.hobby)

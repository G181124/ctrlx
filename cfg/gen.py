import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx cfg --type gen",
        description="Universal config generator / multi-line output",
        epilog="Contoh: --line 'sudo apt update' --line 'sudo apt install nmap'"
    )

    parser.add_argument("--line", action="append", help="Baris konfigurasi atau perintah. Bisa dipakai berkali-kali.")

    args = parser.parse_args(raw_args)

    if not args.line:
        return "[✖] Tidak ada baris (--line) yang diberikan."

    return "[📤] Generated Config:\n" + "\n".join(args.line)

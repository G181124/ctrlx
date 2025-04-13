import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx qrn --type owp",
        description="Generate OSINT-based wordlist from public info",
        epilog="Contoh: --user nopal --platform instagram --info tangerang"
    )

    parser.add_argument("--user", help="Username / nama target")
    parser.add_argument("--platform", help="Platform / sosial media")
    parser.add_argument("--info", help="Tambahan info seperti kota / keyword")

    args = parser.parse_args(raw_args)

    base = []
    if args.user:
        base += [
            args.user,
            args.user + "123",
            args.user + "2023",
            args.user + "2024",
            args.user[::-1]
        ]
    if args.platform:
        base += [
            args.platform,
            args.platform + "01",
            args.platform + "99"
        ]
    if args.info:
        base += [
            args.info,
            args.info + "123",
            args.info[::-1]
        ]

    wordlist = list(set(base))
    return "[📤] Wordlist OSINT:\n" + "\n".join(wordlist)

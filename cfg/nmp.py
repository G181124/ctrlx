import argparse

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx cfg --type nmp",
        description="Generate Nmap custom command from template",
        epilog="Contoh: --target 192.168.1.0/24 --scan syn --script vuln"
    )

    parser.add_argument("--target", required=True, help="Target IP / subnet")
    parser.add_argument("--scan", choices=["syn", "tcp", "udp"], default="syn", help="Tipe scan")
    parser.add_argument("--script", help="Nmap script (optional)")

    args = parser.parse_args(raw_args)

    scan_flag = {
        "syn": "-sS",
        "tcp": "-sT",
        "udp": "-sU"
    }.get(args.scan, "-sS")

    script_part = f"--script={args.script}" if args.script else ""
    command = f"nmap {scan_flag} -Pn -T4 {script_part} {args.target}"

    return f"[📤] Nmap Command:\n{command}"

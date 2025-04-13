## ✅ `README.md` – Versi Final Publik

```markdown
# CTRLX

CTRLX adalah sekumpulan tools baris perintah (CLI) modular berbasis Python, dirancang untuk menunjang eksploitasi, persistence, obfuscation, wordlist, serta otomasi konfigurasi. Seluruh tools dapat dijalankan secara independen, ringan, dan terintegrasi dalam workflow terminal, khususnya di lingkungan Linux seperti Kali Linux.

Tidak memerlukan koneksi ke API eksternal atau autentikasi tambahan. Semua proses berjalan secara lokal dan real-time.

---

## Fitur

- Payload generator untuk Windows, Linux, dan Android
- Stager shell command (bash dan PowerShell)
- Persistence builder: cronjob, systemd, bashrc
- Exploit template generator dan pattern offset tools
- Obfuscator: XOR, base64, hex, chunking, shuffle
- Wordlist generator dari profil, karakter, dan OSINT
- Config builder untuk handler Metasploit dan scanning Nmap

---

## Instalasi

Disarankan menggunakan virtual environment:

```bash
git clone https://github.com/username/ctrlx.git
cd ctrlx
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Penggunaan

```bash
python3 ctrlx.py <kategori> --type <nama_tool> [opsi]
```

Contoh:

```bash
python3 ctrlx.py axt --type w0x --lhost 127.0.0.1 --lport 4444 --format exe --save
```

Bantuan umum:

```bash
python3 ctrlx.py --help
```

Bantuan per kategori:

```bash
python3 ctrlx.py axt --type w0x --help
```

---

## Kategori Tools

| Kategori | Deskripsi |
|----------|-----------|
| `axt`    | Payload dan shellcode generator |
| `rda`    | Persistence dan backdoor tools |
| `zkf`    | Exploit pattern, shellcode, offset |
| `xch`    | Encoder dan obfuscator |
| `qrn`    | Wordlist dan OSINT tools |
| `cfg`    | Builder untuk file konfigurasi dan command |

---

## Contoh Penggunaan

### Membuat payload Windows:
```bash
python3 ctrlx.py axt --type w0x --lhost 192.168.1.10 --lport 4444 --format exe --save
```

### Men-generate cronjob persistence:
```bash
python3 ctrlx.py rda --type c9n --command "/home/user/.hidden/payload.sh" --interval 15 --save
```

### Mengubah shellcode menjadi format variabel Python:
```bash
python3 ctrlx.py zkf --type sch --shellcode "\\x90\\x90\\xcc" --lang python
```

---

## Output

Semua output akan otomatis disimpan ke dalam folder:

```
output/<kategori>/...
```

Contoh:
- `output/axt/payload_127_0_0_1_4444.exe`
- `output/rda/rda_20250412_135632_xxxxxx.txt`
- `output/zkf/zkf_20250412_023732_xxxxxx.txt`

---

## Legal

CTRLX disediakan untuk keperluan edukasi, pelatihan keamanan, dan pengujian pada sistem yang Anda miliki atau memiliki izin eksplisit. Setiap tindakan dan konsekuensi dari penggunaan berada sepenuhnya di tangan pengguna.

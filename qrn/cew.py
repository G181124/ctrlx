import argparse
import requests
from bs4 import BeautifulSoup
import re

def scrape_words(url, min_length):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        words = set(re.findall(r'\b\w{%d,}\b' % min_length, soup.get_text()))
        return '\n'.join(sorted(words))
    except Exception as e:
        return f"[!] Error: {e}"

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx qrn --type cew",
        description="Scrape words from a website to create a wordlist (CeWL-style)",
        epilog="Contoh: python ctrlx.py qrn --type cew --url https://example.com --min 5 --save"
    )

    parser.add_argument("--url", required=True, help="URL website target")
    parser.add_argument("--min", type=int, default=5, help="Minimal panjang kata (default: 5)")

    args = parser.parse_args(raw_args)
    return scrape_words(args.url, args.min)
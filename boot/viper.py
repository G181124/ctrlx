import importlib
import os
import datetime
import random
import string

def random_string(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def save_output(tool_name, output):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{tool_name}_{now}_{random_string()}.txt"
    folder = os.path.join("output", tool_name)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, 'w') as f:
        f.write(output)
    return path

def launch_tool(tool, tool_type, extra_args, save_output=False):
    try:
        module_path = f"{tool}.{tool_type}"
        mod = importlib.import_module(module_path)
        result = mod.run(extra_args)

        path = None
        if save_output:
            path = save_output_file(tool, result)

        return result, path

    except ModuleNotFoundError:
        return f"[!] Modul tidak ditemukan: {tool}/{tool_type}", None
    except Exception as e:
        return f"[!] Terjadi error saat menjalankan tool: {e}", None

def save_output_file(tool_name, output):
    return save_output(tool_name, output)

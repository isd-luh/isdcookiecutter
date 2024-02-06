#!/usr/bin/env python
from pathlib import Path

if __name__ == "__main__":
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        lic_path = Path("./LICENSE").resolve()
        lic_path.unlink()

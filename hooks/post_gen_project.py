#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

if __name__ == "__main__":
    current_dir = Path('.')
    lic_path = current_dir / "{{ cookiecutter.open_source_license }}.txt"
    lic_path.rename("LICENSE")
    for txt_file in current_dir.glob('*.txt'):
        txt_file.unlink()
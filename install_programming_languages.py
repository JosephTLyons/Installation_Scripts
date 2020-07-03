#!/usr/bin/env python3

import os


def install_programming_languages():
    # These installations cover installing languages that aren't installed through homebrew

    # Install Rust
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

    # Install Nim
    os.system("curl https://nim-lang.org/choosenim/init.sh -sSf | sh")


install_programming_languages()

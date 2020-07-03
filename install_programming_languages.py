#!/usr/bin/env python3

import os

from helper_items.helper_functions import install


def install_programming_languages():
    # Install Rust
    install("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

    # Install Nim
    install("curl https://nim-lang.org/choosenim/init.sh -sSf | sh")


install_programming_languages()

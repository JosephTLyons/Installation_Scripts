#!/usr/bin/env python3

import os

def install_programming_languages():
    # These installations cover installing languages that aren't installed through homebrew

    # Install Rust
    os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

    # Install Nim
    os.system("curl https://nim-lang.org/choosenim/init.sh -sSf | sh")

def update_programming_languages():
    # Update Rust
    # Update rustup
    os.system("rustup self update")

    # Updates components:
    # - rustc
    # - rust-std
    # - cargo
    # - rust-docs
    # - rust-analysis
    # - rust-src
    # - rls
    # Then it checks for self updates.  (Is first command needed?)
    os.system("rustup update")

    # Update other components (may no longer be needed)
    os.system("rustup component add clippy")
    os.system("rustup component add rustfmt")

    # Update Nim
    # ?

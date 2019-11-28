#!/usr/bin/env bash

# These installations cover installing languages that aren't installed through homebrew

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install Nim
curl https://nim-lang.org/choosenim/init.sh -sSf | sh
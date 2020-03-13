#!/usr/bin/env python3

import os

# Update Rust --------------------------------------------------------------------------------------

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

# Update Nim ---------------------------------------------------------------------------------------

# ?

#!/usr/bin/env bash

# nim
# ruby - have it installed via curl in non_brew_language_installations

applications=(
    "bash"
    "emacs"
    "git"
    "groff"
    "perl"
    "python"
    "tree"
    "zig"
)

for t in ${applications[@]}; do
    brew install $t
done
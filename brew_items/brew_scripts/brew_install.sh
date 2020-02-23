#!/usr/bin/env bash

# nim
# ruby - have it installed via curl in non_brew_language_installations

applications=(
    "bash"
    "broot"
    "cmake"
    "emacs"
    "git"
    "groff"
    "npm"
    "nushell"
    "perl"
    "pipenv"
    "python"
    "python3"
    "tree"
    "zig"
)

for application in ${applications[@]}; do
    brew install $application
done

#!/usr/bin/env python3

from helper_items.helper_functions import run_command


def install_homebrew():
    install_homebrew_command = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'
    run_command(install_homebrew_command)


install_homebrew()

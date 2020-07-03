#!/usr/bin/env python3

from helper_items.command_lists import brew_applications, pip_applications
from helper_items.helper_functions import batch_run_commands


def install_brew_applications():
    batch_run_commands(brew_applications, command_prefix="brew install ")


def install_pip_applications():
    batch_run_commands(pip_applications, command_prefix="pip3 install ")


install_brew_applications()
install_pip_applications()

#!/usr/bin/env python3

from helper_items.command_lists import brew_application_install_commands, pip_application_install_commands
from helper_items.helper_functions import batch_run_commands


def install_brew_applications():
    batch_run_commands(brew_application_install_commands)


def install_pip_applications():
    batch_run_commands(pip_application_install_commands)


install_brew_applications()
install_pip_applications()

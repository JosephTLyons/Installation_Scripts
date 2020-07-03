#!/usr/bin/env python3

from helper_items.command_lists import brew_cask_application_install_commands
from helper_items.helper_functions import batch_run_commands


def install_brew_cask_applications():
    batch_run_commands(brew_cask_application_install_commands)


install_brew_cask_applications()

#!/usr/bin/env python3

import os

from helper_items.command_lists import programming_language_install_commands
from helper_items.helper_functions import batch_run_commands


def install_programming_languages():
    batch_run_commands(programming_language_install_commands)


install_programming_languages()

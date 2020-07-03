#!/usr/bin/env python3

from helper_items.helper_functions import run_command


def brew_cleanup():
    run_command("brew cleanup")


brew_cleanup()

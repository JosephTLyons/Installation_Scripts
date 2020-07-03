#!/usr/bin/env python3

from helper_items.command_lists import brew_action_commands
from helper_items.helper_functions import batch_run_commands, run_command


def update_and_upgrade_brew():
    batch_run_commands(brew_action_commands)


def update_programming_languages():
    # Update rustup
    run_command("rustup self update")

    # Updates components:
    # - rustc
    # - rust-std
    # - cargo
    # - rust-docs
    # - rust-analysis
    # - rust-src
    # - rls
    # Then it checks for self updates.  (Is first command needed?)
    run_command("rustup update")

    # Update other components (may no longer be needed)
    run_command("rustup component add clippy")
    run_command("rustup component add rustfmt")

    # Update Nim
    # ?


update_and_upgrade_brew()
update_programming_languages()

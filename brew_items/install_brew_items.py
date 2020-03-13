#!/usr/bin/env python3

import os

# Install homebrew if it isn't installed
# command -v brew >/dev/null 2>&1 || { /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" }

do_you_wish_to = "Do you wish to"
install = "install:"
command_line_applications = "command line applications"
brew_install = "(brew install)"
installing = "Installing:"

def action(question, log_message, command):
    print(question + "?")
    answer = input()

    if answer in ["y", "Y"]:
        print(log_message)
        os.system(command)

action(
    do_you_wish_to + " " + install + " " + command_line_applications + " " + brew_install,
    installing + " " + command_line_applications + " " + brew_install,
    "./brew_items/brew_scripts/brew_install.py"
)

gui_applications = "GUI Applications"
brew_cask_install = "(brew cask install)"

action(
    do_you_wish_to + " " + install + " " + gui_applications + " " + brew_cask_install,
    installing + " " + gui_applications + " " + brew_cask_install,
    "./brew_items/brew_scripts/brew_install.py"
)

your_brew_related_items = "your brew-related items"

action(
    do_you_wish_to + " update and upgrade " + your_brew_related_items,
    "Updating and upgrading " + your_brew_related_items,
    "./brew_items/update_and_upgrade_brew.py"
)

action(
    do_you_wish_to + " brew clean",
    "brew cleaning",
    "brew cleanup"
)

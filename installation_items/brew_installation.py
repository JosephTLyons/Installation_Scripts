#!/usr/bin/env python3

import os

from .application_lists import command_line_applications, gui_applications

def __install_applications(install_command, applications):
    for application in applications:
        os.system("{install_command} {application}".format(install_command=install_command, application=application))

def __brew_install_command_line_applications():
    __install_applications("brew install", command_line_applications)

def __brew_install_gui_applications():
    __install_applications("brew cask install", gui_applications)

def __brew_cleanup():
    os.system("brew cleanup")

def update_and_upgrade_brew():
    actions = [
        "update",
        "upgrade",
        "cask upgrade",
    ]

    for action in actions:
        os.system("brew {action}".format(action=action))

def __action(action_message, log_message, function):
    print("Do you wish to " + action_message + "?")

    if input() in ["y", "Y"]:
        print(log_message)
        function()

def install_brew_items():
    # Install homebrew if it isn't installed
    # command -v brew >/dev/null 2>&1 || { /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" }

    install = "install:"
    installing = "Installing:"
    command_line_applications = "command line applications"
    brew_install = "(brew install)"

    __action(
        install + " " + command_line_applications + " " + brew_install,
        installing + " " + command_line_applications + " " + brew_install,
        __brew_install_command_line_applications
    )

    gui_applications = "GUI Applications"
    brew_cask_install = "(brew cask install)"

    __action(
        install + " " + gui_applications + " " + brew_cask_install,
        installing + " " + gui_applications + " " + brew_cask_install,
        __brew_install_gui_applications
    )

    your_brew_related_items = "your brew-related items"

    __action(
        "update and upgrade " + your_brew_related_items,
        "Updating and upgrading " + your_brew_related_items,
        update_and_upgrade_brew
    )

    __action("brew clean", "brew cleaning", __brew_cleanup)

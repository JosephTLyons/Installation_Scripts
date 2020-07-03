#!/usr/bin/env python3

from .lists import brew_applications, brew_actions,  brew_cask_applications, pip_applications


brew_action_commands = [("brew " + brew_action) for brew_action in brew_actions]


brew_application_install_commands = [("brew install " + brew_application) for brew_application in brew_applications]


brew_cask_application_install_commands = [("brew cask install " + brew_cask_application) for brew_cask_application in brew_cask_applications]


pip_application_install_commands = [("pip3 install " + pip_application) for pip_application in pip_applications]


# Break out non-curl stuff similar to lists above?
programming_language_install_commands = [
    "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
    "curl https://nim-lang.org/choosenim/init.sh -sSf | sh",
]

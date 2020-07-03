#!/usr/bin/env python3

from helper_items.helper_functions import install_applications
from helper_items.application_lists import brew_applications, pip_applications


def install_brew_applications():
    install_applications("brew install", brew_applications)


def install_pip_applications():
    install_applications("pip3 install", pip_applications)


install_brew_applications()
install_pip_applications()

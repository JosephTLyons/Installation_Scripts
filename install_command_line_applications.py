#!/usr/bin/env python3

from helper_items.application_lists import brew_applications, pip_applications
from helper_items.helper_functions import batch_install


def install_brew_applications():
    batch_install("brew install", brew_applications)


def install_pip_applications():
    batch_install("pip3 install", pip_applications)


install_brew_applications()
install_pip_applications()

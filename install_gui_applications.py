#!/usr/bin/env python3

from helper_items.application_lists import brew_cask_applications
from helper_items.helper_functions import batch_install


def install_brew_cask_applications():
    batch_install("brew cask install", brew_cask_applications)


install_brew_cask_applications()

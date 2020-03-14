#!/usr/bin/env python3

import os

from installation_items.brew_installation import install_brew_items
from installation_items.programming_languages import install_programming_languages

install_brew_items()
install_programming_languages()

# deal with non-brew stuff
# conditional checks for installing brew and non-brew stuff
# dotfiles and symlinks
# pip stuff?
# editor settings and plugins

# Recall to clean up folders and repo of rust scripts that are now somewhat included in here

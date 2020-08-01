#!/usr/bin/env python3

from .lists import brew_applications, brew_taps, brew_update_actions,  brew_cask_applications, \
    pip_applications, programming_language_curl_items


brew_update_action_commands = [("brew " + brew_action) for brew_action in brew_update_actions]


brew_tap_commands = [("brew tap " + brew_tap) for brew_tap in brew_taps]


brew_application_install_commands = [("brew install " + brew_application) for brew_application in brew_applications]


brew_cask_application_install_commands = [("brew cask install " + brew_cask_application) for brew_cask_application in brew_cask_applications]


pip_application_install_commands = [("pip3 install " + pip_application) for pip_application in pip_applications]


programming_language_install_commands = [("curl " + programming_language_curl_item) for programming_language_curl_item in programming_language_curl_items]

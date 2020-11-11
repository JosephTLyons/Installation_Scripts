#!/usr/bin/env python3

from .lists import (
    brew_applications,
    brew_taps,
    brew_update_actions,
    brew_cask_applications,
    mas_application_name_and_mas_application_identifier_tuple_list,
    pip_applications,
    programming_language_curl_items,
)


brew_update_action_commands = [f"brew {brew_action}" for brew_action in brew_update_actions]


brew_tap_commands = [f"brew tap {brew_tap}" for brew_tap in brew_taps]


brew_application_install_commands = [
    f"brew install {brew_application}" for brew_application in brew_applications
]


brew_cask_application_install_commands = [
    f"brew cask install {brew_cask_application}" for brew_cask_application in brew_cask_applications
]


mas_application_install_command_and_command_output_tuple_list = [
    (f"mas install {mas_application_identifier}", f"mas install {mas_application_name}")
    for mas_application_name, mas_application_identifier in mas_application_name_and_mas_application_identifier_tuple_list
]


pip_application_install_commands = [
    f"pip3 install {pip_application}" for pip_application in pip_applications
]


programming_language_install_commands = [
    f"curl {programming_language_curl_item}"
    for programming_language_curl_item in programming_language_curl_items
]

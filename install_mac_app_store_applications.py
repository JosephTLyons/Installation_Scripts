#!/usr/bin/env python3

from helper_items.command_lists import mas_application_install_command_and_command_output_tuple_list
from helper_items.helper_functions import run_command


# Run the same command for installing or updating
def install_mac_app_store_applications():
    for (
        mas_application_install_command,
        command_output,
    ) in mas_application_install_command_and_command_output_tuple_list:
        run_command(mas_application_install_command, command_output)


install_mac_app_store_applications()

#!/usr/bin/env python3

import os


def batch_run_commands(command_items, command_prefix=None):
    for command_item in command_items:
        command = ""

        if command_prefix is not None:
            command = command_prefix

        command += "{command_item}".format(command_item=command_item)

        run_command(command)


def run_command(command):
    print(command)
    os.system(command)

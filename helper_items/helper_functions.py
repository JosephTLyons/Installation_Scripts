#!/usr/bin/env python3

import os


def batch_run_commands(commands):
    for command in commands:
        run_command(command)


def run_command(command):
    print(command)
    os.system(command)

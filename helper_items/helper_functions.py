#!/usr/bin/env python3

import os


def batch_install(install_command, applications):
    for application in applications:
        command = "{install_command} {application}".format(install_command=install_command, application=application)
        install(command)

def install(install_command):
    print(install_command)
    os.system(install_command)

#!/usr/bin/env python3

import os


def install_applications(install_command, applications):
    for application in applications:
        command = "{install_command} {application}".format(install_command=install_command, application=application)
        print(command)
        os.system(command)

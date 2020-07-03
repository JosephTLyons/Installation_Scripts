#!/usr/bin/env python3

import os


def install_applications(install_command, applications):
    print(install_command)

    for application in applications:
        print("    {application}".format(application=application))
        command = "{install_command} {application}".format(install_command=install_command, application=application)
        # os.system(command)

    print()

#!/usr/bin/env python3

import os

applications = [
    "bash",
    "broot",
    "cmake",
    "emacs",
    "git",
    "groff",
    "neofetch",
    "npm",
    "nushell",
    "perl",
    "pipenv",
    "python",
    "python3",
    "tree",
    "zig",
]

for application in applications:
    os.system("brew install {application}".format(application=application))

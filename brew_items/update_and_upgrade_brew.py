#!/usr/bin/env python3

import os

actions = [
    "update",
    "upgrade",
    "cask upgrade",
]

for action in actions:
    os.system("brew {action}".format(action=action))

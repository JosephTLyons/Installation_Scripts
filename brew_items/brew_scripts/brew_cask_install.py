#!/usr/bin/env python3

import os

applications = [
    "android-studio",
    "atom",
    "blender",
    "cutter",
    "cyberduck",
    "db-browser-for-sqlite",
    "discord",
    "dropbox",
    "duet",
    "emacs",
    "firefox",
    "fork",
    "github",
    "go2shell",
    "google-chrome",
    "intellij-idea-ce",
    "licecap",
    "mactex",
    "malwarebytes",
    "microsoft-excel",
    "microsoft-powerpoint",
    "microsoft-teams",
    "microsoft-word",
    "pycharm-ce",
    "reaper",
    "slack",
    "sourcetree",
    "steam",
    "sublime-merge",
    "ti-connect-ce",
    "unity",
    "visual-studio-code",
]

for application in applications:
    os.system("brew install {application}".format(application=application))

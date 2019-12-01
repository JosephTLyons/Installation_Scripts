#!/usr/bin/env bash

applications=(
    "android-studio"
    "atom"
    "blender"
    "cutter"
    "cyberduck"
    "db-browser-for-sqlite"
    "discord"
    "dropbox"
    "duet"
    # "emacs" this conflicts with the command line version, runing emacs <filename> launches the GUI version
    "firefox"
    "fork"
    "github"
    "go2shell"
    "google-chrome"
    "intellij-idea-ce"
    "licecap"
    "malwarebytes"
    "microsoft-excel"
    "microsoft-powerpoint"
    "microsoft-teams"
    "microsoft-word"
    "pycharm-ce"
    "reaper"
    "slack"
    "sourcetree"
    "steam"
    "sublime-merge"
    "ti-connect-ce"
    "unity"
    "visual-studio-code"
)

for application in ${applications[@]}; do
    brew cask install $t
done
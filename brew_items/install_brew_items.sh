#!/usr/bin/env bash

# Install homebrew if it isn't installed
# command -v brew >/dev/null 2>&1 || { /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" }

do_you_wish_to="Do you wish to"
install="install: "
command_line_applications="command line applications"
brew_install="(brew install)"
installing="Installing: "

echo $do_you_wish_to $install $command_line_applications $brew_install"?"
read answer

if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
    echo $installing $command_line_applications $brew_install

    ./brew_items/brew_scripts/brew_install.sh
fi

gui_applications="GUI Applications"
brew_cask_install="(brew cask install)"

echo $do_you_wish_to $install $gui_applications $brew_cask_install"?"
read answer

if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
    echo $installing $gui_applications $brew_cask_install

    ./brew_items/brew_scripts/brew_cask_install.sh
fi

your_brew_related_items="your brew-related items"

echo $do_you_wish_to "update and upgrade" $your_brew_related_items"?"
read answer

if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
    echo "Updating and upgrading" $your_brew_related_items

    ./brew_items/brew_scripts/update_and_upgrade_brew.sh
fi

echo $do_you_wish_to "brew clean?"
read answer

if [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
    echo "brew cleaning"

    brew cleanup
fi
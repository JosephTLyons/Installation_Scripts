#!/usr/bin/env python3

import os

from installation_items.brew_installation import update_and_upgrade_brew
from installation_items.programming_languages import update_programming_languages

update_and_upgrade_brew()
update_programming_languages()

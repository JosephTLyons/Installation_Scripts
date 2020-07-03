import os


def update_and_upgrade_brew():
    actions = [
        "update",
        "upgrade",
        "cask upgrade",
    ]

    for action in actions:
        os.system("brew {action}".format(action=action))


def update_programming_languages():
    # Update rustup
    os.system("rustup self update")

    # Updates components:
    # - rustc
    # - rust-std
    # - cargo
    # - rust-docs
    # - rust-analysis
    # - rust-src
    # - rls
    # Then it checks for self updates.  (Is first command needed?)
    os.system("rustup update")

    # Update other components (may no longer be needed)
    os.system("rustup component add clippy")
    os.system("rustup component add rustfmt")

    # Update Nim
    # ?


update_and_upgrade_brew()
update_programming_languages()

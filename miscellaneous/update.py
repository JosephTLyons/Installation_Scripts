from helper_items.helper_functions import run_command


def update_and_upgrade_brew():
    actions = [
        "update",
        "upgrade",
        "cask upgrade",
    ]

    for action in actions:
        run_command("brew {action}".format(action=action))


def update_programming_languages():
    # Update rustup
    run_command("rustup self update")

    # Updates components:
    # - rustc
    # - rust-std
    # - cargo
    # - rust-docs
    # - rust-analysis
    # - rust-src
    # - rls
    # Then it checks for self updates.  (Is first command needed?)
    run_command("rustup update")

    # Update other components (may no longer be needed)
    run_command("rustup component add clippy")
    run_command("rustup component add rustfmt")

    # Update Nim
    # ?


update_and_upgrade_brew()
update_programming_languages()

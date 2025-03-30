import os

from bluer_objects import file, README

from blue_ai import NAME, VERSION, ICON, REPO_NAME


def build():
    return README.build(
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
        MODULE_NAME=NAME,
    )

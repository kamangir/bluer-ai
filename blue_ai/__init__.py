import os

NAME = "blue_ai"

ICON = "🪄"

DESCRIPTION = f"{ICON} A language to speak AI."

VERSION = "11.8.1"

REPO_NAME = "blue-ai"

MARQUEE = "https://github.com/kamangir/assets/blob/main/awesome-bash-cli/marquee-2024-10-26.jpg?raw=true"


def fullname() -> str:
    abcli_git_branch = os.getenv("abcli_git_branch", "")
    return "{}-{}{}".format(
        NAME,
        VERSION,
        f"-{abcli_git_branch}" if abcli_git_branch else "",
    )

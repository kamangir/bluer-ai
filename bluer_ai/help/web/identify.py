from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.web import is_accessible


def help_identify(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "count=3",
            xtra(",~log,", mono=mono),
            "loop",
            xtra(",sleep=5,", mono=mono),
            "timestamp",
        ]
    )

    args = is_accessible.args

    return show_usage(
        [
            "@web",
            "identify",
            f"[{options}]",
        ]
        + args,
        "identify web connection.",
        mono=mono,
    )

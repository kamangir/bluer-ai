from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.web import is_accessible


def help_identify(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "loop",
            xtra(",~upload", mono=mono),
        ]
    )

    args = sorted(
        [
            "[--sleep <5>]",
            "[--timestamp 0]",
        ]
        + is_accessible.args
    )

    return show_usage(
        [
            "@web",
            "identify",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "identify web connection.",
        mono=mono,
    )

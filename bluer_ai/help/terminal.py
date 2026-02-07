from typing import List

from bluer_options.terminal import show_usage, xtra


def help_badge(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "clear,reset,save"

    return show_usage(
        [
            "@badge",
            f"[{options}]",
            '"🌀"',
        ],
        "update badge.",
        mono=mono,
    )

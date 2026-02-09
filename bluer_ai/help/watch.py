from typing import List

from bluer_options.terminal import show_usage, xtra


def options(
    mono: bool,
    cascade: bool = False,
) -> str:
    return "".join(
        [
            xtra(
                "{}count=<count>,{}".format(
                    "" if cascade else "~clear,",
                    "" if cascade else "dryrun,error=while|until,~hr,~log,",
                ),
                mono=mono,
            ),
            "loop," if cascade else "",
            xtra(
                "seconds=<seconds>",
                mono=mono,
            ),
        ]
    )


def help_watch(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@watch",
            f"[{options(mono=mono)}]",
            "<command-line>",
        ],
        "watch <command-line>.",
        mono=mono,
    )

from typing import List

from bluer_options.terminal import show_usage
from bluer_options.web.access.vars import dict_of_variables

from bluer_ai.help.watch import options as watch_options


def help_check(
    tokens: List[str],
    mono: bool,
) -> str:
    options = watch_options(
        mono=mono,
        cascade=True,
    )

    args = [
        "[--timeout 3]",
    ]

    return show_usage(
        [
            "@web",
            "access",
            "check",
            "[<url> | all]",
            f"[{options}]",
        ]
        + args,
        "check web access.",
        mono=mono,
    )


def help_log(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@web",
            "access",
            "log",
        ],
        "log web access.",
        mono=mono,
    )


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@web",
            "access",
            "set",
            " | ".join(sorted(dict_of_variables.keys())),
            "0 | 1",
        ],
        "set web access.",
        {
            "{}: {} (currently: {})".format(
                keyword,
                info["name"],
                info["value"],
            ): ""
            for keyword, info in dict_of_variables.items()
        },
        mono=mono,
    )


help_functions = {
    "check": help_check,
    "log": help_log,
    "set": help_set,
}

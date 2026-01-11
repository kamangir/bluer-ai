from typing import List

from bluer_options.terminal import show_usage, xtra


def help_get_ip(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@web",
            "get_ip",
        ],
        "get IP.",
        mono=mono,
    )


is_args = [
    "[--timeout 3]",
]


def help_identify(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~upload,", mono=mono),
            "loop",
        ]
    )

    args = sorted(
        [
            "[--sleep <30>]",
        ]
        + is_args
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


def help_is_accessible(
    tokens: List[str],
    mono: bool,
) -> str:

    return show_usage(
        [
            "@web",
            "is_accessible",
            "<url>",
        ]
        + is_args,
        "is <url> accessible?",
        mono=mono,
    )


def help_where_am_i(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@web",
            "where_am_i",
        ],
        "where am I?",
        mono=mono,
    )


help_functions = {
    "get_ip": help_get_ip,
    "identify": help_identify,
    "is_accessible": help_is_accessible,
    "where_am_i": help_where_am_i,
}

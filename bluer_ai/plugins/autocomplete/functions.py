import os
from typing import List, Dict


def autocomplete(
    command: str,
    cword: int,
    words: List[str],
    alias_filename: str,
    debug_output: bool = True,
) -> List[str]:
    dict_of_aliases = read_aliases(alias_filename)

    command = dict_of_aliases.get(command, command)

    if len(words) >= 1:
        words[0] = dict_of_aliases.get(words[0], words[0])

    if debug_output:
        with open(
            "{}/autocomplete.log".format(os.getenv("HOME")),
            "w",
        ) as f:
            f.write(
                "\n".join(
                    [
                        ",".join(
                            [
                                "{}={}".format(key, value)
                                for key, value in dict_of_aliases.items()
                            ]
                        ),
                        "",
                        f"command={command}",
                        f"cword={cword}",
                        f"words={words}",
                        "---\n",
                    ]
                )
            )

    return [word.strip() for word in words]


def read_aliases(alias_filename: str) -> Dict[str, str]:
    full_path = os.path.join(
        os.path.dirname(__file__),
        alias_filename,
    )

    with open(full_path, "r", encoding="utf-8") as f:
        list_of_aliases = f.readlines()

    dict_of_aliases = {
        alias: reference
        for alias, reference in [
            line.strip().split("=", 1) for line in list_of_aliases if "=" in line
        ]
    }

    dict_of_aliases = {
        alias.replace("alias ", "").strip(): reference
        for alias, reference in dict_of_aliases.items()
    }

    return dict_of_aliases

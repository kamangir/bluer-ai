import os
import argparse

from blueness import module

from bluer_ai import NAME
from bluer_options.autocomplete import autocomplete

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--command",
    type=str,
)
parser.add_argument(
    "--cword",
    type=int,
)
parser.add_argument(
    "--words",
    type=str,
)
parser.add_argument(
    "--alias_filename",
    type=str,
)
args = parser.parse_args()

print(
    " ".join(
        autocomplete(
            command=args.command,
            cword=args.cword,
            words=args.words.strip().split(),
            alias_filename=os.path.join(
                os.path.dirname(__file__),
                args.alias_filename,
            ),
        )
    )
)

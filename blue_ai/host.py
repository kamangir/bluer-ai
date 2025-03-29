from typing import List

from blue_options.host import signature as blue_options_signature
from blue_objects import fullname as blue_objects_fullname

from blue_ai import fullname


def signature() -> List[str]:
    return [
        fullname(),
        blue_objects_fullname(),
    ] + blue_options_signature()

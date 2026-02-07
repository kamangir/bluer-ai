import requests

from blueness import module
from bluer_options import string
from bluer_options.timing import ElapsedTimer

from bluer_ai import NAME
from bluer_ai.logger import logger


NAME = module.name(__file__, NAME)


def is_accessible(
    url,
    timeout: int = 3,
    verbose: bool = False,
) -> bool:
    if verbose:
        logger.info(
            "{}.is_accessible[timeout={}]({})?".format(
                NAME,
                string.pretty_duration(
                    timeout,
                    short=True,
                ),
                url,
            )
        )

    success = False
    elapsed_timer = ElapsedTimer()
    try:
        response = requests.get(
            url,
            timeout=timeout,
        )
        success = response.status_code == 200
    except Exception as e:
        if verbose:
            logger.warning(e)

    if verbose:
        logger.info(
            "{} in {}.".format(
                "succeeded" if success else "failed",
                elapsed_timer.as_str(),
            )
        )

    return success

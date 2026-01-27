from typing import Dict
import time

from blueness import module
from bluer_options import string
from bluer_objects.metadata import post_to_object

from bluer_ai import NAME
from bluer_ai.web.status.get import get_status
from bluer_ai.logger import logger

NAME = module.name(__file__, NAME)


def get_status_on_a_loop(
    object_name: str,
    timeout: int = 3,
    log: bool = False,
    count: int = -1,
    sleep: int = 30,
    timestamp: bool = False,
) -> bool:
    logger.info(
        "{}.get_status_on_a_loop: timeout={}{}, sleep:{} -{}> {}".format(
            NAME,
            string.pretty_duration(timeout),
            "" if count == -1 else f", {count} sample(s)",
            string.pretty_duration(sleep),
            "timestamp-" if timestamp else "",
            object_name,
        )
    )

    list_of_status: Dict[float, str] = {}
    try:
        while True:
            list_of_status[string.pretty_date()] = get_status(
                timeout=timeout,
                log=log,
                timestamp=timestamp,
            )

            if count != -1 and len(list_of_status) > count:
                logger.info(f"{count} samples collected.")
                break

            time.sleep(sleep)
    except KeyboardInterrupt:
        logger.warning("Ctrl+C, stopping.")
    except Exception as e:
        logger.error(e)
        return False

    logger.info("collected {} sample(s).".format(len(list_of_status)))

    return post_to_object(
        object_name,
        "status",
        list_of_status,
    )

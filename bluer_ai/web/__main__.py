import argparse
from typing import Dict
import time

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_options import string
from bluer_objects.metadata import post_to_object

from bluer_ai import NAME
from bluer_ai.web.status import get_status
from bluer_ai.web.accessible import is_accessible
from bluer_ai.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="identify | is_accessible",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
    help="-1: forever",
)
parser.add_argument(
    "--log",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--loop",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--period",
    type=int,
    default=30,
    help="in seconds",
)
parser.add_argument(
    "--timeout",
    type=int,
    default=3,
    help="in seconds",
)
parser.add_argument(
    "--url",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "is_accessible":
    print(
        int(
            is_accessible(
                args.url,
                timeout=args.timeout,
            )
        )
    )
elif args.task == "identify":
    success = True

    list_of_status: Dict[float, str] = {}
    counter = 0
    if args.loop:
        try:
            while True:
                count += 1
                list_of_status[string.pretty_date()] = get_status(
                    timeout=args.timeout,
                    log=args.log == 1,
                )

                if args.count != -1 and count > args.count:
                    logger.info(f"{args.count} samples collected.")
                    break

                time.sleep(args.period)
        except KeyboardInterrupt:
            logger.warning(f"Ctrl+C, stopping.")
        except Exception as e:
            logger.error(e)
            success = False

        if success:
            success = post_to_object(
                args.object_name,
                "status",
                list_of_status,
            )

    else:
        status = get_status(
            timeout=args.timeout,
            log=args.log == 1,
        )
        print(status)
else:
    success = None

sys_exit(logger, NAME, args.task, success)

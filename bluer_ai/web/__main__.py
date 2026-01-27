import argparse


from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ai import NAME
from bluer_ai.web.status.get import get_status
from bluer_ai.web.status.loop import get_status_on_a_loop
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
    default=-1,
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
    "--sleep",
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
    "--timestamp",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--url",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "is_accessible":
    success = True
    print(
        int(
            is_accessible(
                args.url,
                timeout=args.timeout,
            )
        )
    )
elif args.task == "identify":
    if args.loop:
        success = get_status_on_a_loop(
            timeout=args.timeout,
            log=args.log != 0,
            count=args.count,
            sleep=args.sleep,
            object_name=args.object_name,
            timestamp=args.timestamp == 1,
        )
    else:
        success = True
        print(
            get_status(
                timeout=args.timeout,
                log=args.log == 1,
                timestamp=args.timestamp == 1,
            )
        )
else:
    success = None

sys_exit(logger, NAME, args.task, success)

from bluer_options import string

from bluer_ai import env
from bluer_ai.plugins.web.accessible import is_accessible
from bluer_ai.logger import logger

dict_of_status = {
    "national": "🇮🇷",
    "offline": "⛓️‍💥",
    "online": "🛜",
}


def get_status(
    timeout: int = 3,
    log: bool = False,
    timestamp: bool = False,
) -> str:
    status = (
        "offline"
        if not is_accessible(
            env.BLUER_AI_INTERNET_ONLINE_CHECK_URL,
            timeout=timeout,
        )
        else (
            "national"
            if not is_accessible(
                env.BLUER_AI_INTERNET_NATIONAL_CHECK_URL,
                timeout=timeout,
            )
            else "online"
        )
    )

    if log:
        logger.info(
            "{}{} {}".format(
                (
                    "{} ".format(
                        string.timestamp(
                            unique_length=0,
                        )
                    )
                    if timestamp
                    else ""
                ),
                dict_of_status.get(status, "❓"),
                status,
            )
        )

    return status

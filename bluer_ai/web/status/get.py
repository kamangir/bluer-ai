from bluer_ai import env
from bluer_ai.web.accessible import is_accessible
from bluer_ai.logger import logger


def get_status(
    timeout: int = 3,
    log: bool = False,
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
        if status == "online":
            logger.info("🛜 online.")

        if status == "national":
            logger.info("🇮🇷 internet is national.")

        if status == "offline":
            logger.info("⛓️‍💥 offline.")

    return status

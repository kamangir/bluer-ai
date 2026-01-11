from bluer_options.testing import are_nonempty_strs

from bluer_ai import env


def test_bluer_ai_env():
    assert are_nonempty_strs(
        [
            env.BLUER_AI_INTERNET_ONLINE_CHECK_URL,
            env.BLUER_AI_INTERNET_NATIONAL_CHECK_URL,
        ]
    )

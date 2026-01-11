from bluer_ai.web.status import identify


def test_web_identification():
    assert isinstance(identify(log=True), str)

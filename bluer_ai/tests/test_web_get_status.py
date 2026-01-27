from bluer_ai.plugins.web.status.get import get_status


def test_web_get_status():
    assert isinstance(get_status(log=True), str)

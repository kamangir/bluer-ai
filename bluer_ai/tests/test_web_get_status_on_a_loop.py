from bluer_objects import objects

from bluer_ai.plugins.web.status.loop import get_status_on_a_loop


def test_web_get_status_on_a_loop():
    object_name = objects.unique_object("test_web_get_status_on_a_loop")

    assert get_status_on_a_loop(
        object_name,
        timeout=3,
        log=False,
        count=3,
        sleep=5,
    )

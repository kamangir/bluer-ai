from bluer_objects.README.items import ImageItems, Items
from bluer_objects.README.consts import assets_url
from bluer_objects import markdown

docs = [
    {
        "path": "../docs/web.md",
        "macros": {
            "items_receive:::": markdown.generate_table(
                ImageItems(
                    {
                        assets_url(
                            suffix=f"bluer-ai-web/web-receive-{index:02}.jpg",
                            volume=2,
                        ): ""
                        for index in range(1, 9)
                    }
                ),
                cols=8,
                log=False,
            ),
            "items_send:::": markdown.generate_table(
                Items(
                    [
                        {
                            "name": name,
                            "marquee": assets_url(
                                suffix=f"bluer-ai-web/web-send-{index+1:02}.jpg",
                                volume=2,
                            ),
                        }
                        for index, name in enumerate(
                            [
                                "http://192.168.43.61:8000/",
                                "http://192.168.43.61:8000/test-00.png",
                                "http://192.168.43.61:8000/test.json",
                            ]
                        )
                    ]
                ),
                cols=3,
                log=False,
            ),
        },
    }
]

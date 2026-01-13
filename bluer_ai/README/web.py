from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets, assets_url
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
                ImageItems(
                    {
                        assets_url(
                            suffix=f"bluer-ai-web/web-send-{index:02}.jpg",
                            volume=2,
                        ): ""
                        for index in range(1, 4)
                    }
                ),
                cols=3,
                log=False,
            ),
        },
    }
]

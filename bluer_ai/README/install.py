from bluer_ai.env import BLUER_AI_SBC_PASSWORD

docs = [
    {
        "path": f"../docs/install/{kind}.md",
        "macros": {
            "password:::": BLUER_AI_SBC_PASSWORD,
        },
    }
    for kind in [
        "ec2",
        "Jetson-Nano",
        "macOS",
        "RPi-ROS",
        "RPi",
        "SageMaker",
    ]
]

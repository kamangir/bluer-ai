from flask import Flask, request
import os
import argparse

from blueness import module
from bluer_objects import file
from bluer_objects import objects

from bluer_ai import env
from bluer_ai import NAME, ICON
from bluer_ai.host import signature

NAME = module.name(__file__, NAME)

app = Flask(__name__)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--path",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--port_receive",
    type=str,
    default=env.BLUER_AI_WEB_RECEIVE_PORT,
)
parser.add_argument(
    "--port_send",
    type=str,
    default=env.BLUER_AI_WEB_SEND_PORT,
)
args = parser.parse_args()

app.config["UPLOAD_FOLDER"] = args.path


@app.route("/")
def upload_form():
    success, html = file.load_text(
        file.absolute(
            "./app.html",
            file.path(__file__),
        )
    )
    if not success:
        return "❗️ app.html not found."

    form = "\n".join(html)

    for this, that in {
        "{icon}": ICON,
        "{IP}": env.BLUER_AI_IP,
        "{logo}": env.BLUER_AI_WEB_LOGO,
        "{port_receive}": args.port_receive,
        "{port_send}": args.port_send,
        "{footer}": " | ".join(signature()),
        "{header}": (
            ""
            if args.object_name == "void"
            else " | ".join(
                objects.signature(
                    object_name=args.object_name,
                )
            )
        ),
    }.items():
        form = form.replace(this, that)

    return form


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if file.filename:
        file.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename,
            ),
        )
        return 'uploaded. ✅ | <a href="../">upload another file ...</a>.'

    return '⚠️ file not found | <a href="../">go back ...</a>.'


app.run(
    host="0.0.0.0",
    port=int(args.port_receive),
)

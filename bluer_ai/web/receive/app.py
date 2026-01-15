from flask import Flask, request
import os
import argparse

from blueness import module
from bluer_ai.env import BLUER_AI_IP

from bluer_ai import env
from bluer_ai import NAME

NAME = module.name(__file__, NAME)

app = Flask(__name__)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--path",
    type=str,
)
parser.add_argument(
    "--port",
    type=int,
    default=env.BLUER_AI_WEB_RECEIVE_PORT,
)
args = parser.parse_args()

app.config["UPLOAD_FOLDER"] = args.path


@app.route("/")
def upload_form():
    return """
    🔗 <a href="http://{}:{}/">http://{}:{}/</a><hr/>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="upload">
    </form>
    """.format(
        BLUER_AI_IP,
        args.port,
        BLUER_AI_IP,
        args.port,
    )


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
    port=args.port,
)

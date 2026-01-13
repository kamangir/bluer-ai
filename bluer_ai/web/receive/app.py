from flask import Flask, request
import os
import argparse

from blueness import module

from bluer_ai import NAME

NAME = module.name(__file__, NAME)

app = Flask(__name__)


@app.route("/")
def upload_form():
    return """
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="upload">
    </form>
    """


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save(
        os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename,
        ),
    )
    return "uploaded. ✅"


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--path",
    type=str,
)
parser.add_argument(
    "--port",
    type=int,
    default=8001,
)
args = parser.parse_args()

app.config["UPLOAD_FOLDER"] = args.path

app.run(
    host="0.0.0.0",
    port=args.port,
)

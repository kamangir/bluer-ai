from flask import Flask, request
import os

from bluer_options.env import get_env


app = Flask(__name__)
UPLOAD_FOLDER = get_env("BLUER_AI_WEB_RECEIVE_PATH")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def upload_form():
    return """
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="آپلود">
    </form>
    """


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return "فایل با موفقیت آپلود شد!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

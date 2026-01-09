from flask import Flask, render_template, request
from backend.speech_to_text import speech_to_text
from backend.text_to_gloss import text_to_gloss
from backend.gloss_to_video import gloss_to_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gloss_videos = []
    text = ""

    if request.method == "POST":
        audio = request.files["audio"]
        path = "temp.wav"
        audio.save(path)

        text = speech_to_text(path)
        gloss = text_to_gloss(text)
        gloss_videos = gloss_to_video(gloss)

        os.remove(path)

    return render_template("index.html", text=text, videos=gloss_videos)

if __name__ == "__main__":
    app.run(debug=True)

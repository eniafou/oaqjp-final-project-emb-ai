""" Emotion Detection Flask Server """

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """ homepage endpoint """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """ endpoint for emotion detection """
    sentence = request.args.get("textToAnalyze")
    emotions = emotion_detector(sentence)

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant_emotion = emotions["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    text = request.args.get("textToAnalyze")
    if not text:
        return "Error: No text provided", 400

    emotions = emotion_detector(text)  # should return a dictionary

    if emotions is None:
        return "Error: Could not compute emotions", 500

    response = (
        f"anger: {emotions.get('anger', 0.0)}, "
        f"disgust: {emotions.get('disgust', 0.0)}, "
        f"fear: {emotions.get('fear', 0.0)}, "
        f"joy: {emotions.get('joy', 0.0)}, "
        f"sadness: {emotions.get('sadness', 0.0)}, "
        f"dominant_emotion: {emotions.get('dominant_emotion','unknown')}"
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)

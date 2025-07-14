# server.py
from flask import Flask, request, jsonify
from EmotionDetection.EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Flask endpoint to detect emotions from the string in 
    'textToAnalyze' query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "No text provided. Please provide 'textToAnalyze' as a query parameter."}), 400

    detections = emotion_detector(text_to_analyze)

    if detections is None:
        return jsonify({"error": "Invalid input provided for emotion detection."}), 400

    return jsonify(detections)

@app.route("/")
def index():
    """
    Informative message for root URL
    """
    return "Welcome to the Emotion Detector API! Use /emotionDetector?textToAnalyze=<your_text>"

port = 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
'''
This module provides a server using the emotion_detection function. It defines a URL for 
submission of text, and returns English text identifying the dominant emotion. It deals 
gracefully with the error of missing text.
'''
from flask import Flask, request
from EmotionDetection.EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Flask endpoint to detect emotions from the string in 
    'textToAnalyze' query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    detections = emotion_detector(text_to_analyze)
    # Find dominant emotion
    biggest_prob = -1
    dominant_emotion = None
    for emotion in detections:
        prob = detections[emotion]
        if prob is not None:
            if prob > biggest_prob:
                dominant_emotion = emotion
                biggest_prob = detections[emotion]
    # Deal with error case first
    if dominant_emotion is None:
        return " Invalid text! Please try again!"
    # Generate output string if valid dominant emotion
    output = "For the given statement, the system response is "
    for emotion in detections:
        prob = detections[emotion]
        output = output + "'"+emotion+"': "+ str(prob) +", "
    output = output[:-2] + ". The dominant emotion is " + str(dominant_emotion) + "."

    # return string output
    return output

@app.route("/")
def index():
    """
    Informative message for root URL
    """
    return "Welcome to the Emotion Detector API! Use /emotionDetector?textToAnalyze=<your_text>"

PORT = 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
    
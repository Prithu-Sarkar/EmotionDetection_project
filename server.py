"""
Flask server for the Emotion Detector web application.
Provides web interface and API endpoint for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route handler for emotion detection.
    Accepts text via query parameter and returns emotion analysis.

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or error message for blank input.
    """
    text_to_analyse = request.args.get('textToAnalyse')

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return output


@app.route("/")
def render_index_page():
    """
    Renders the main index page.

    Returns:
        str: Rendered HTML of index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Emotion Detector - Final Project

## Project Name: Emotion Detection Application using Watson NLP

This project is an AI-based web application that detects emotions from text using IBM Watson NLP libraries. It identifies emotions such as **anger**, **disgust**, **fear**, **joy**, and **sadness** from a given text input and returns the dominant emotion.

## Features
- Detect 5 core emotions: anger, disgust, fear, joy, sadness
- Returns the dominant emotion with scores
- Web-based UI using Flask
- Error handling for blank inputs
- Unit tested and statically analyzed (pylint score: 10/10)

## Project Structure

```
EmotionDetection_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Technologies Used
- Python 3.x
- IBM Watson NLP Library (via Watson Embedded AI)
- Flask (Web Framework)
- PyLint (Static Code Analysis)
- unittest (Unit Testing)

## How to Run
1. Clone the repository
2. Install dependencies: `pip install flask requests`
3. Run the server: `python server.py`
4. Open browser: `http://localhost:5000`

"""
Unit tests for the emotion_detector function.
Tests dominant emotion detection for various emotional inputs.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit test class for emotion_detector function."""

    def test_joy_emotion(self):
        """Test that joy is detected as dominant emotion for a joyful statement."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Test that anger is detected as dominant emotion for an angry statement."""
        result = emotion_detector("I am really angry at this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Test that disgust is detected as dominant emotion for a disgusting statement."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Test that sadness is detected as dominant emotion for a sad statement."""
        result = emotion_detector("It is really sad this happened")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Test that fear is detected as dominant emotion for a fearful statement."""
        result = emotion_detector("I am scared to death because of this")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for dominant_emotion."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()

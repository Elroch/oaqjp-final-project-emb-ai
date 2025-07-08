# Unit tests
from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def dominant_emotion(self, text):
        emotions = emotion_detector(text)
        best = -1
        for emotion in emotions:
            if emotions[emotion] > best:
                best_emotion = emotion
                best = emotions[emotion]
        return best_emotion
    def test_joy(self):
        self.assertEqual(self.dominant_emotion("I am glad this happened"), "joy")

    def test_anger(self):
        self.assertEqual(self.dominant_emotion("I am really mad about this"), "anger")

    def test_disgust(self):
        self.assertEqual(self.dominant_emotion("I feel disgusted just hearing about this"), "disgust")

    def test_sadness(self):
        self.assertEqual(self.dominant_emotion("I am so sad about this"), "sadness")

    def test_fear(self):
        self.assertEqual(self.dominant_emotion("I am really afraid that this will happen"), "fear")

if __name__ == '__main__':
    unittest.main()
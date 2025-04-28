import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy_emotion(self):
        """Test that joy is correctly detected as the dominant emotion"""
        result = emotion_detector("I am glad this happened")
        print(result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger_emotion(self):
        """Test that anger is correctly detected as the dominant emotion"""
        result = emotion_detector("I am really angry about this")
        print(result)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust_emotion(self):
        """Test that disgust is correctly detected as the dominant emotion"""
        result = emotion_detector("I feel disgusted just hearing about this")
        print(result)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness_emotion(self):
        """Test that sadness is correctly detected as the dominant emotion"""
        result = emotion_detector("I am so sad about this")
        print(result)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear_emotion(self):
        """Test that fear is correctly detected as the dominant emotion"""
        result = emotion_detector("I am very afraid this will happen")
        print(result)
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()

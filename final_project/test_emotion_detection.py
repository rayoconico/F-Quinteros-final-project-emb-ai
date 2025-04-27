import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_positive_emotion(self):
        text = "Me alegra que esto haya sucedido"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_negative_emotion(self):
        text = "Estoy realmente enojado por esto"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        text = "Me siento disgustado solo de oír sobre esto"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        text = "Estoy tan triste por esto"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        text = "Tengo mucho miedo de que esto suceda"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

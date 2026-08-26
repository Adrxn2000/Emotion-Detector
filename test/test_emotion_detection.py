import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am so angry with you")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("This is disgusting")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am scared of the dark")
        self.assertEqual(result['dominant_emotion'], 'fear')

        result = emotion_detector("I am so sad today")
        self.assertEqual(result['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()

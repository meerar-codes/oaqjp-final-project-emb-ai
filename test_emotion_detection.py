from EmotionDetection import emotion_detector

def test_emotions():
    """
    This function tests emotion detection for multiple inputs.
    """

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected_emotion in test_cases.items():
        result = emotion_detector(text)
        dominant = result['dominant_emotion']

        print(f"Input: {text}")
        print(f"Expected: {expected_emotion}, Got: {dominant}")

        assert dominant == expected_emotion, f"Test failed for: {text}"

    print("All tests passed!")

if __name__ == "__main__":
    test_emotions()
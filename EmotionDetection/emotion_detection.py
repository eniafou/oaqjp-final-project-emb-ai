import requests
import json

def emotion_detector(text_to_analyze):
    response = requests.post(
        url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={
            "raw_document": {
                "text": text_to_analyze
            }
        }
    )

    data = json.loads(response.text)

    emotions = data["emotionPredictions"][0]["emotion"]

    dominant_emotion = "joy"
    highest_score = 0

    for emotion in emotions:
        emotion_score = emotions[emotion]
        if emotion_score > highest_score:
            dominant_emotion = emotion
            highest_score = emotion_score

    emotions["dominant_emotion"] = dominant_emotion

    return emotions
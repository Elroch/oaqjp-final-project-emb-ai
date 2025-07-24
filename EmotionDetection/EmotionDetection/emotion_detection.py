import requests, json

# Task 3
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    # Sending a POST request to the emotion detector API
    response = requests.post(url, json=input_json, headers=header)
    # Convert to json format for processing
    formatted_response = json.loads(response.text)
    # Extract emotion probability evaluations
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Deal with status code 400
    if response.status_code == 400:
        emotions = {"anger": None, "disgust": None, "fear": None, 
        "joy": None, "sadness": None}
    return emotions

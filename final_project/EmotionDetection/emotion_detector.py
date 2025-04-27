import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Enviamos la solicitud POST
    response = requests.post(url, json=input_json, headers=headers)
    
    # Verificamos si la respuesta fue exitosa
    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parseamos la respuesta JSON
    response_data = response.json()
    
    # Extraemos las emociones y la emoción dominante
    emotions = response_data['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Formateamos la salida como se requiere
    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': dominant_emotion
    }

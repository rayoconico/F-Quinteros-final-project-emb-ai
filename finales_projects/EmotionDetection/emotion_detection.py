import requests
import json

def emotion_detector(text_to_analyze):
    # URL del servicio de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Encabezados para la solicitud
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Crear el cuerpo de la solicitud JSON
    input_json = { 
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Enviar la solicitud POST
    response = requests.post(url, json=input_json, headers=headers)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        response_data = response.json()
        
        # Extraer las emociones desde la respuesta
        emotions = response_data['emotionPredictions'][0]['emotion']
        
        # Determinar la emoción dominante (la emoción con el puntaje más alto)
        dominant_emotion = max(emotions, key=emotions.get)

        # Retornar el formato solicitado
        return {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
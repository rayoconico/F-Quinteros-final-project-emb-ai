"""
server.py

Este archivo contiene el servidor Flask que maneja las peticiones POST a la ruta '/emotionDetector'.
Utiliza la función 'emotion_detector' para detectar emociones en un texto dado.

Dependencias:
    - Flask
    - EmotionDetection (función emotion_detector)
    - requests (para manejar errores de conexión)

Funciones:
    - detect_emotion: Maneja las peticiones POST y devuelve las emociones detectadas.
"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import requests  # Aquí importamos 'requests'

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Recibe un texto por POST y detecta la emoción dominante utilizando el modelo de Watson NLP.

    Retorna:
        dict: Un diccionario con las emociones detectadas y la emoción dominante.
    """
    try:
        data = request.get_json()
        text_to_analyze = data.get("text", "")

        if not text_to_analyze.strip():
            return jsonify(message="¡Texto inválido! ¡Por favor, intenta de nuevo!"), 400

        emotions = emotion_detector(text_to_analyze)

        if emotions["dominant_emotion"] is None:
            return jsonify(message="¡Texto inválido! ¡Por favor, intenta de nuevo!"), 400

        response_message = (
            f"Para la declaración dada, la respuesta del sistema es "
            f"'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, "
            f"'joy': {emotions['joy']}, "
            f"'sadness': {emotions['sadness']}. "
            f"La emoción dominante es {emotions['dominant_emotion']}."
        )

        return jsonify(message=response_message)

    except (requests.exceptions.RequestException, ValueError) as e:
        # Captura excepciones más específicas
        print(f"Error: {e}")
        return jsonify(message="¡Ocurrió un error en el servidor!"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

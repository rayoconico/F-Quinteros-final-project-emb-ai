from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    text_to_analyze = request.form["text"]
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"
    else:
        result = (f"Para la declaración dada, la respuesta del sistema es "
                  f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                  f"'fear': {response['fear']}, 'joy': {response['joy']}, "
                  f"y 'sadness': {response['sadness']}. "
                  f"La emoción dominante es {response['dominant_emotion']}.")
        return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

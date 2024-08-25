from flask import Flask, render_template, request, jsonify
from stress_relief_bot import StressReliefBot
import speech_recognition as sr
import tempfile
import os

app = Flask(__name__)
bot = StressReliefBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_message = request.args.get('msg')
    return jsonify(response=bot.get_response(user_message))

@app.route('/activity', methods=['GET'])
def get_activity():
    return jsonify(response=bot.suggest_activity())

@app.route('/voice', methods=['POST'])
def voice_input():
    if 'audio' not in request.files:
        return jsonify(error="No audio file received")
    
    file = request.files['audio']
    
    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_audio:
        file.save(temp_audio.name)
        temp_audio_path = temp_audio.name

    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(temp_audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        bot_response = bot.get_response(text)
        os.unlink(temp_audio_path)  # Delete the temporary file
        return jsonify(response=bot_response, transcription=text)
    except sr.UnknownValueError:
        os.unlink(temp_audio_path)  # Delete the temporary file
        return jsonify(error="Could not understand audio")
    except sr.RequestError:
        os.unlink(temp_audio_path)  # Delete the temporary file
        return jsonify(error="Could not request results from speech recognition service")
    except Exception as e:
        os.unlink(temp_audio_path)  # Delete the temporary file
        return jsonify(error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import speech_recognition as sr
from gtts import gTTS
import os

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Initialize ChatBot
chatbot = ChatBot('StressReliefBot')
trainer = ListTrainer(chatbot)
trainer.train([
    "I'm feeling stressed.",
    "I'm sorry to hear that. Would you like to try some breathing exercises?",
    "Yes.",
    "Great! Try inhaling deeply for 4 seconds, hold for 4 seconds, and exhale slowly."
])

# Initialize NLP and Translator
nlp = pipeline("sentiment-analysis")
translator = Translator()

conversation_context = []
user_profiles = {
    "user1": {"name": "Dinesh"}
}
crisis_keywords = ['self-harm', 'suicide', 'hopeless']

# Preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    return filtered_tokens

# Analyze sentiment
def analyze_sentiment(text):
    result = nlp(text)[0]
    return result['label'], result['score']

# Update conversation context
def update_context(user_input):
    conversation_context.append(user_input)
    if len(conversation_context) > 10:
        conversation_context.pop(0)

# Suggest a breathing exercise
def suggest_breathing_exercise():
    return "Try this: Inhale for 4 seconds, hold for 4, exhale for 4."

# Provide personalized quote
def get_personalized_quote(user_id):
    return f"Keep pushing, {user_profiles[user_id]['name']}. You're doing great!"

# Crisis intervention
def crisis_intervention(text):
    if any(keyword in text for keyword in crisis_keywords):
        return "It seems you might need immediate help. Please contact a mental health professional or call emergency services."
    return None

# Handle input and generate response
def handle_input(user_input, user_id="user1", lang='en'):
    translated_input = translator.translate(user_input, dest='en').text
    update_context(translated_input)
    crisis_message = crisis_intervention(translated_input)
    
    if crisis_message:
        return personalize_response(user_id, crisis_message, lang)
    
    response = chatbot_response_logic(conversation_context)
    return personalize_response(user_id, response, lang)

# Personalize response with user's name
def personalize_response(user_id, response, lang):
    if user_id in user_profiles:
        response = f"{user_profiles[user_id]['name']}, {response}"
    return translator.translate(response, dest=lang).text

# Chatbot response logic based on context and sentiment
def chatbot_response_logic(context):
    if "stressed" in context[-1]:
        return "It sounds like you're stressed. How about trying a breathing exercise?"
    elif analyze_sentiment(context[-1])[0] == "NEGATIVE":
        return suggest_breathing_exercise()
    else:
        return "I'm here to help. What's on your mind?"

# Speech recognition for voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."

# Convert text to speech
def text_to_speech(text, lang='en'):
    tts = gTTS(text=translator.translate(text, dest=lang).text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)
    os.system(f"mpg321 {filename}")

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')
    user_id = request.args.get('user_id', 'user1')
    lang = request.args.get('lang', 'en')
    response = handle_input(user_input, user_id, lang)
    return jsonify({'response': response})

@app.route('/voice', methods=['POST'])
def voice_interaction():
    user_id = request.form.get('user_id', 'user1')
    lang = request.form.get('lang', 'en')
    user_input = recognize_speech()
    response = handle_input(user_input, user_id, lang)
    text_to_speech(response, lang)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)

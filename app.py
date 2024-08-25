from flask import Flask, render_template, request
from transformers import pipeline
from nltk.chat.util import Chat, reflections
from gtts import gTTS
import os
import random
import nltk

nltk.download('punkt')

app = Flask(__name__)

# Chatbot logic
pairs = [
    ['my name is (.*)', ['Hello %1, how can I assist you today?']],
    ['(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hey!']],
    ['(.*) weather (.*)', ['I am unable to check the weather, but I hope it’s sunny!']],
    ['(.*) (location|city) ?', ['I am in the cloud, everywhere and nowhere!']],
    ['(.*) your name ?', ['My name is ChatBot.']],
    ['how are you ?', ['I am just a bunch of code, but thanks for asking!']],
    ['(.*) created you ?', ['I was created by a team of developers.']],
    ['(.*) help (.*)', ['I can assist you with general questions.']],
    ['quit', ['Goodbye!']]
]

chatbot = Chat(pairs, reflections)
sentiment_pipeline = pipeline('sentiment-analysis')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = chatbot.respond(userText)
    return str(bot_response)

@app.route("/get_sentiment")
def get_sentiment_response():
    userText = request.args.get('msg')
    sentiment = sentiment_pipeline(userText)[0]
    return f"Sentiment: {sentiment['label']}, Confidence: {sentiment['score']:.2f}"

@app.route("/get_audio")
def get_audio_response():
    userText = request.args.get('msg')
    tts = gTTS(text=userText, lang='en')
    filename = "temp.mp3"
    tts.save(filename)
    return f"Audio file saved as {filename}"

if __name__ == "__main__":
    app.run()

import wolframalpha
import os
import wikipedia
from gtts import gTTS
import json
from pygame import mixer
import requests     
import sys
from weather import Weather
from weather import Unit
import geocoder
from chatterbot import ChatBot

app_id = "YERQA8-KG2P6T357L"
client = wolframalpha.Client(app_id)
chatbot = ChatBot(
    'Hari',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )
chatbot.train("chatterbot.corpus.english")

def chat():
    while True:
        user_input = input("> ")
        output = chatbot.get_response(user_input)
        print(output)
        input()

def fetch():
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=21d02c03cbd143d8a65fab4bac5f181f"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"]+str(" - ")+ar["description"])
            
    for i in range(len(results)):
        print(i + 1, results[i]) 
        tts = gTTS(results[i])
        tts.save("news.mp3")
        os.system("afplay news.mp3")
        os.remove("news.mp3")


while True:
    query = input("> ")
    
    if "latest" in query and "news" in query or "news" in query:
        fetch()

    if query == "":
        print("invalid command!")

    if query == "quit" or query == "exit":
        break
        sys.exit()

    if "chat" in query and "with" in query and "me" in query:
        chat()

    if "weather" in query:
        g = geocoder.ip('me')
        lat, lng = g.latlng
        weather = Weather(unit=Unit.CELSIUS)
        lookup = weather.lookup_by_latlng(lat, lng)
        condition = lookup.condition
        print(condition)
        
    try:
        result = client.query(query)
        answer = next(result.results).text
        print(answer)
        tts = gTTS(answer)
        tts.save("results.mp3")
        os.system("afplay results.mp3")
        os.remove("results.mp3")
        

    except:
        query = query.split(' ')
        query = " ".join(query[2:])
        answer = wikipedia.summary(query, sentences=3)
        print(answer)
        tts = gTTS(answer)
        tts.save("resultss.mp3")
        os.system("afplay resultss.mp3")
        os.remove("resultss.mp3")
import datetime
import os
import time
import webbrowser
import smtplib
import numpy as np
import pandas as pd
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
from pygame import mixer
import pickle

filename = 'personal_info'
outfile = open(filename, 'wb')
os.system('cls')
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
file = open('personal_info', 'rb')
data = pickle.load(file)
file.close()
mail_adress=data[3]
url = ('http://newsapi.org/v2/top-headlines?'
       'q=trump&'
       'country=us&'
       'sortBy=popularity&'
       'apiKey=04c1bbbdf4d04fac97e83e086bc5e803')
response = requests.get(url)
response_dict = response.json()
for x in response_dict:
    if x == 'articles':
        response_list = response_dict[x]


def talk(text):
    engine.say(text)
    engine.runAndWait()


def starting():
    global hour
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        talk("Hi,good morning,sir!")
    elif 12 <= hour < 18:
        talk("Hello, Have a good afternoon,sir. I'm TRON, Your personal assistant. How may I help you today?")
    else:
        talk("Hello, Have a good day. Sir")


def take_komut():
    try:
        with sr.Microphone() as source:
            print("listening")
            talk("I'm listening to you sir")
            voice = listener.listen(source)
            komut = listener.recognize_google(voice)
            komut = komut.lower()
            if 'alexa' in komut:
                komut = komut.replace('alexa', '')
                print(komut)
    finally:
        pass
    return komut

def articles():
    talk('\n\nthe articles are :')
    for i in response_list:
        talk('\n\n')
        for key in i:
            talk(i['title'])
            break
def run_tron():
    if __name__ == '__main__':
        komut = take_komut()
        print(komut)
        if 'play' in komut:
            sarki = komut.replace('play', '')
            talk('playing ' + sarki)
            pywhatkit.playonyt(sarki)
        elif 'open youtube' in komut:
            webbrowser.open_new_tab("https://www.youtube.com")
            talk("Youtube is open now")
        elif 'open google' in komut:
            webbrowser.open_new_tab("https://www.google.com")
            talk("Google chrome is open now")
        elif 'open gmail' in komut:
            webbrowser.open_new_tab("gmail.com")
            talk("Gmail  is open now")
        elif 'open hotmail' in komut:
            webbrowser.open_new_tab("outlook.com")
            talk("Hotmail is open now")
        elif 'time' in komut:
            global time
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'date' in komut:
            date = datetime.datetime.now().strftime('%A:%d:%B:%Y')
            talk("Today's date is: " + date)
        elif 'how are you' in komut or "what's going on" in komut or "what's up" in komut:
            talk("Fine. How about you")
        elif 'joke' in komut:
            talk(pyjokes.get_joke())
        if 'wikipedia' in komut:
            talk('Searching Wikipedia...')
            komut = komut.replace("wikipedia", "")
            results = wikipedia.summary(komut, sentences=3)
            talk("According to Wikipedia")
            print(results)
            talk(results)
        elif 'thank you' in komut or "thanks" in komut:
            talk("My pleasure, Sir.")
        elif "weather" in komut:
            api_key = "c97d9114d6d01707228670c8326536b1"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            talk("whats the city name")
            city_name = take_komut()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] == "404":
                talk(" City Not Found ")
            else:
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                talk(" Temperature in kelvin unit is " +
                     str(current_temperature) +
                     "\n humidity in percentage is " +
                     str(current_humidity) +
                     "\n description  " +
                     str(weather_description))

        elif 'news' in komut:
            talk('What type of news do you want ? Please give me a specific answer, Sir.')
        elif 'cryptocurrencies' in komut:
            news = webbrowser.open_new_tab("https://www.coindesk.com/news")
            talk('Here are the latest news from the crypto world have fun,Sir.')
        elif 'world' in komut:
            news = webbrowser.open_new_tab("https://www.bbc.com/news/world")
            talk('Here are the latest news from all over the world have fun,Sir.')
        elif 'political' in komut:
            news = webbrowser.open_new_tab("https://www.coindesk.com/news")
            talk('Here are the latest news from the politics world have fun,Sir.')
        elif 'sports' in komut:
            news = webbrowser.open_new_tab("https://www.coindesk.com/news")
            talk('Here are the latest news from the sports world have fun,Sir.')
        elif 'tech and it' in komut:
            news = webbrowser.open_new_tab("https://www.coindesk.com/news")
            talk('Here are the latest news from the tech and it world have fun,Sir.')
        elif 'science' in komut:
            news = webbrowser.open_new_tab("https://www.coindesk.com/news")
            talk('Here are the latest news from the crypto world have fun,Sir.')
        elif 'entertainment and arts' in komut:
            news = webbrowser.open_new_tab("https://www.coindesk.com/news")
            talk('Here are the latest news from the crypto world have fun,Sir.')
        elif 'ask' in komut:
            talk('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = take_komut()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            talk(answer)
            print(answer)
        elif 'search' in komut:
            komut = komut.replace("search", "")
            webbrowser.open_new_tab(komut)
        elif 'who are you' in komut or 'what can you do' in komut:
            talk(
                "Hello, I'm TRON. Your favourite personal assistant. I can answer to all of your questions. I can play"
                "songs and find the song with its lyrics. I can check wikipedia and google for you. I can bring news to"
                "your household. I can also support you with daily essentials like weather and sending e mails .")

        elif "email" in komut:
            talk("What is the subject?")
            time.sleep(3)
            subject = take_komut()
            talk("What should I say?")
            message = take_komut()
            content = "Subject: {}\n\n{}".format(subject, message)
            talk("Who would you want to mail, sir.")
            to = take_komut()
            user_mail=mail_adress
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("fatihserdarogludosyapaylasim@gmail.com", "112Fatih112")
            mail.sendmail(mail_adress, to, content)
            mail.close()

            talk("Email sent.")

        elif "hi" in komut or "hello" in komut or "sup" in komut:
            talk("Hello!.")

        elif "hot" in komut:
            articles()

        elif "goodbye" in komut or "okay bye" in komut or "stop" in komut:
            talk("Shutting down  the service. Goodbye,Sir.")
            exit()
        elif 'wait' in komut:
            talk("I'm waiting you sir")
            time.sleep(10)
        else:
            talk(
                "I couldn't hear you. Or the phrase is not supported yet. Please contact developers. If you want to "
                "shut me down  just say: wait")
starting()
while True:
    run_tron()

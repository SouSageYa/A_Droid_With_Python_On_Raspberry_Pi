import speech_recognition as sr
import pyttsx3
import os
import pickle
import time
filename = 'Personalinfo'
outfile = open(filename, 'wb')
os.system('cls')
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_komut():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            komut = listener.recognize_google(voice)
            komut = komut.lower()
    finally:
        pass
    return komut
komut = take_komut()
time.sleep(10)
if 'alexa setup' in komut:
    talk(
        "Hello,dear sir. Welcome to TRON Setup interface. I will ask you some questions to optimize myself. "
        "Please answer the questions step by step.")
    talk("Your name and surname")
    komut = take_komut()
    print(komut)
    if 'my name is' in komut or "i am" in komut or "this is " in komut:
        person = komut.replace('Name and surname', '')
        pickle.dump(person, outfile)
        talk("Next up can I have the date of your birth. Firstly year")
    else:
        talk("Please give me a valid answer")
        talk("Shutting down please retry")
        exit()
    komut = take_komut()
    print(komut)
    if 'birth year' in komut or 'year' in komut or 'it is' in komut:
        birth_year = komut.replace('Birth year', '')
        pickle.dump(birth_year, outfile)
        talk("Can I have the month please.")
    else:
        talk("Please give me a valid answer")
        talk("Shutting down please retry")
        exit()
    komut = take_komut()
    print(komut)
    if 'birth month' in komut or 'month' in komut or 'it is' in komut:
        birth_month = komut.replace('Birth month', '')
        pickle.dump(birth_month, outfile)
        talk("And finally your birthday")
    else:
        talk("Please give me a valid answer")
        talk("Shutting down please retry")
        exit()
    komut = take_komut()
    print(komut)
    if 'birth day' in komut or 'day' in komut or 'it is' in komut:
        birth_day = komut.replace('Birth day', '')
        pickle.dump(birth_day, outfile)
        talk("Next up mail information. Your Mail adress")
    else:
        talk("Please give me a valid answer")
        talk("Shutting down please retry")
        exit()
    komut = take_komut()
    print(komut)
    if 'gmail.com' in komut or "outlook.com" in komut or "hotmail.com" in komut or "yahoo.com" in komut or "att.com" in komut or "comcast.com" in komut or "verizon.com" in komut:
        mail_adress = komut.replace('Mail adress', '')
        pickle.dump(mail_adress, outfile)
        talk("for multiple adresses please enter them while sending an e-mail")
        talk("Next up your password. Use password keyword")
        outfile.close()
    else:
        talk("Please give me a valid answer")
        talk("Shutting down please retry")
        exit()

os.system('2.py')

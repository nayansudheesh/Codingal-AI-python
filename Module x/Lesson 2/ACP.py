import speech_recognition as sr

import pyttsx3
import requests
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
def get_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"you said : {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("could not understand what you said")
    except sr.RequestError as e:
        print(f"API error: {e}")
    return ""
def respond_to_command(command):
    if "hello" in command:
        speak("i am your voice assistant , how may i help you today?")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"the time is {now}")
    elif "date" in command:
        today = datetime.now().strftime("%Y-%m-%d")
        speak(f"the date is {today}")
    elif "day" in command:
        day = datetime.now().strftime("%A")
        speak(f"today is {day}")
    elif "fun facts" in command:
        try:
            response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
            if response.status_code == 200:
                fact = response.json().get("text")
                speak(f"here's a fun fact: {fact}")
            else:
                speak("sorry, i couldn't fetch a fun fact right now.")
        except Exception as e:
            speak(f"error occured: {e}")
    elif "exit"  in command:
        speak("goodbye! nice meeting you!")
        
        return False
    else:
        speak("i cannot help you with that right now")

def main():
    speak("voice assistant activated , say something to get started")

    while True:
        command =  get_audio()

        if command and not respond_to_command(command):
                break
if __name__ == "__main__":
    main()
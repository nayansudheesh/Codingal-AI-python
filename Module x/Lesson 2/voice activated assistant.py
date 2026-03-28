import speech_recognition as sr

import pyttsx3

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
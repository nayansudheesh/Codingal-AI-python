import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text):
    engine = pyttsx3.init()
    engine.setproperty('rate', 150)
    voices = engine.getproperty('voices')

    if language == 'en':
        engine.setproperty('voice', voices[0].id)
    else:
        engine.setproperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak into your microphone in english")
        audio = recognizer.listen(source)
    try:
        print("recognizing specech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"you said: {text}")
        return text
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print(f"API Error:  {e}")
def translate_text(text, dest_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def display_language_options():
    print("select a language:")
    print("1. hindi")
    print("2. tamil")
    print("3. telugu")
    print("4. bengali")
    print("5. marathi")
    print("6. gujarati")
    print("7. malayalam")
    print("8. punjabi")

    choice = input("enter the target language number: (1-8)")

    language_dict = {
        '1': 'hi',
        '2': 'ta',
        '3': 'te',
        '4': 'bn',
        '5': 'mr',
        '6': 'gu',
        '7': 'ml',
        '8': 'pa'
    }
    return language_dict.get(choice, 'es')  
def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, dest_language=target_language)
        speak(translated_text , language = "en")
        print("transalation spoken out")

if __name__ == "__main__":
    main()

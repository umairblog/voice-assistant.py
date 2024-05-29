import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import datetime
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()


def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't get that."
    except sr.RequestError:
        return "Sorry, I couldn't connect to the recognition service."

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what's the time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "play" in command:
        query = command.replace("play", "").strip()
        search_url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(search_url)
    else:
        speak("Sorry, I didn't understand that.")

if _name_ == "_main_":
    speak("hello dear.what I can do for you?")
    while True:
        command = recognize_speech().lower()
        print("You said:", command)
        handle_command(command)
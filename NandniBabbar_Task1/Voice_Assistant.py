import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)
recognizer = sr.Recognizer()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening..")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language='en_US').lower()
            print(f'You: {text}')
            return text
        except:
            return ""

def process(text):
    if 'chrome' in text:
        speak('Opening Chrome')
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
    elif 'time' in text:
        speak(datetime.datetime.now().strftime('%I:%M %p'))
    elif 'play' in text:
        speak('Playing on YouTube')
        pywhatkit.playonyt(text)
    elif 'youtube' in text:
        speak('Opening YouTube')
        webbrowser.open('https://www.youtube.com')
    elif 'google' in text:
        speak('Opening Google')
        webbrowser.open('https://www.google.com')
    elif 'exit' in text or 'bye' in text:
        speak('Goodbye')
        return False
    return True

speak("Hello, I'm ready")
while True:
    command = listen()
    if command and not process(command):
        break
    
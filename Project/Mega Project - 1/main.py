import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

engine = pyttsx3.init()
API_KEY = "5e6f563f0f75455eae95afb8dff76a6f"

def say(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command:
        webbrowser.open("https://www.twitter.com")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
    elif "open stackoverflow" in command:
        webbrowser.open("https://www.stackoverflow.com")
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
    elif "open whatsapp" in command:
        webbrowser.open("https://www.whatsapp.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            
            for article in articles:
                say (article["title"])
    
    elif "exit" in command or "quit" in command:
        say("Goodbye!")
        exit()
    else:
        # let open Ai handle this
        pass

if __name__ == '__main__':
    say("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            try:
                print("Listening for the keyword 'Jarvis'...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                if command.lower() == "jarvis":
                    say("Yes?")
                    print("Waiting for further commands...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
            except sr.UnknownValueError:
                print("Sorry, I did not understand the audio.")
            except sr.RequestError as e:
                print(f"Request error from Google Speech API: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

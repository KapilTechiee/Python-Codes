import wikipedia
import pywhatkit
from datetime import datetime
from speech import speak

def respond_to_command(command):
    """Process user commands"""
    if "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")

    elif "exit" in command:
        speak("Goodbye! Kapil Sir Have A Good Dayyyy Wohhh")
        exit()

    else:
        speak("I'm not sure how to do that yet.")

import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except:
        speak("Sorry, I didn't catch that. Please repeat.")
        return ""

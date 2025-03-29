from speech import take_command, speak
from commands import respond_to_command

speak("Heyyy Kapill Sir How Are You! I am JARVIS. How can I assist you today?")

while True:
    user_command = take_command()
    respond_to_command(user_command)

# this is a program where whatever you type will be spoken by your computer
# this will run on windows
import pyttsx3

print("Welcome, i am RoboSpeaker2.0, >_< ")
while True:
    to_speak = input("Enter what you want me to speak (or type q to quit): ")
    if to_speak == 'q':
        engine = pyttsx3.init()
        engine.say("Goodbye")
        engine.runAndWait()
        print("Goodbye...")
        break
    engine = pyttsx3.init()
    engine.say(to_speak)
    engine.runAndWait()
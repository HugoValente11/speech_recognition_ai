import pyglet
import speech_recognition as sr
from command import Commander

ERROR_COMMAND = "Couldn't make out what you said"


def say(text):
    command = Commander()

    if not running:
        command.respond("Goodbye")

    elif text != ERROR_COMMAND:
        command.discover(text)

    else:
        command.respond(ERROR_COMMAND)

def play_sound(int):
    if int:
        file = pyglet.resource.media('audio/begin.mp3')

    else:
        file = pyglet.resource.media('audio/end.mp3')

    file.play()


# obtain audio from the microphone
r = sr.Recognizer()


def init_speech():
    print("Listening...")
    play_sound(1)

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    play_sound(0)

    try:
        command = r.recognize_google(audio)

    except:
        command = ERROR_COMMAND

    print(command)

    if command in ["quit", "goodbye", "exit", "bye"]:
        global running
        running = False
    say(command)


running = True
while running:
    init_speech()

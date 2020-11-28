import pyttsx3
import os
from get_answer import Fetcher

engine = pyttsx3.init()


class Commander:
    def __init__(self):
        self.confirm = ["yes", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "your" in text:
                response = "My name is pie commander."
            elif "my" in text:
                response = "You still haven't told me your name."
            else:
                response = "Sorry didn't catch what you said."
            self.respond(response)

        if "open" in text:
            application = text.split(' ', 1)[-1]
            self.respond("Opening " + application)
            os.system("start " + application)

        else:
            base_url_search = "https://www.google.com/search?q="
            text = text.replace(" ", "+")
            fetcher = Fetcher(base_url_search + text)
            answer = fetcher.lookup()
            self.respond(answer)

    def respond(self, response):
        engine.say(response)
        engine.runAndWait()

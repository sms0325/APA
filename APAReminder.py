import time
class Reminder:
    def __init__(self, title, snooze, rtype, window=""):
        self.title = title
        self.snooze = snooze
        self.rtype = rtype
        self.window = window
        self.done = False
    def yes(self):
        self.done = True

    def snz(self):
        time.sleep(snooze * 60)

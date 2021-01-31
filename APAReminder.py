import time
class Reminder:
    def __init__(self, title,snooze,rtype,window=""):
        self.title = title
        self.snooze = snooze
        self.rtype = rtype
        self.window = window
        self.done = False
        self.show = True
    
    def yes():
        self.done = True

    def snz()
        time.sleep(snooze * 60)

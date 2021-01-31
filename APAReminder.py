import time
import asyncio
from APAGraphics import GUIButton, GUIPrompt
'''class Reminder:
    def __init__(self, title, snooze, rtype, window=""):
        self.title = title
        self.snooze = snooze
        self.rtype = rtype
        self.window = window
        self.done = False
        self.yesBtn = GUIButton("Yes", lambda: self.yes())
        self.snoozeBtn = GUIButton("Snooze", lambda: self.snz())
        #self.prompt = GUIPrompt(title, self.yesBtn, self.snoozeBtn)
    
    async def start(self):
        prompt = GUIPrompt(title, self.yesBtn, self.snoozeBtn)
        await asyncio.sleep(1)
        while not self.done:
            prompt.show("Did you finish this task?")
        
    def yes(self):
        self.done = True

    async def snz(self):
        await asyncio.sleep(snooze * 60)
        print("Snoozed")'''

class Reminder:
    def __init__(self, title, snooze, rtype, window=""):
        self.title = title
        self.snooze = snooze
        self.rtype = rtype
        self.window = window
        self.done = False
        self.yesBtn = GUIButton("Yes", lambda: self.yes())
        self.snoozeBtn = GUIButton("Snooze", lambda: self.snz())
        #self.prompt = GUIPrompt(title, self.yesBtn, self.snoozeBtn)
    
    async def start(self):
        prompt = GUIPrompt(self.title, self.yesBtn, self.snoozeBtn) #ask Meslissa about how to pass in master
        await asyncio.sleep(1)
        prompt.show("Did you finish this task?")
        
    def yes(self):
        self.done = True

    async def snz(self):
        await asyncio.sleep(self.snooze * 60)
        print("Snoozed", self.title)
        prompt.show("Did you finish this task?")


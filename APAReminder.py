import time
import asyncio
from APAGraphics import GUIButton, GUIPrompt

class Reminder:
    def __init__(self, master, title, snooze, queue):
        self.master = master
        self.title = title
        self.snooze = snooze
        self.done = False
        self.queue = queue
        self.yesBtn = GUIButton("Yes", self.yes)
        self.snoozeBtn = GUIButton("Snooze", self.snz)
        self.prompt = GUIPrompt(self.master, self.title, self.yesBtn, self.snoozeBtn)
    
    async def start(self):
        await asyncio.sleep(1)
        self.queue.put(self.prompt.show("Did you finish this task?"))
        print("Put on queue")
        
    def yes(self):
        print("yes")
        self.done = True

    async def snz(self):
        print("Before Snoozing")
        await asyncio.sleep(self.snooze * 60)
        print("Snoozed", self.title)
        self.queue.put(self.prompt.show("Did you finish this task?"))
        print("Put on queue")


from APAGraphics import GUIButton, GUIPrompt
from APAReminder import *
import time
import asyncio
import tkinter as tk

root = tk.Tk()

rems = []

rems.append(Reminder(root,"Finish modules",1))
rems.append(Reminder(root,"Read textbook",1))

async def main():
    for r in rems:
        asyncio.ensure_future(r.start())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
pending = asyncio.all_tasks()
loop.run_until_complete(asyncio.gather(*pending))

root.mainloop()
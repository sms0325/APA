from APAGraphics import GUIButton, GUIPrompt, GUIProcessor, GUIMascot
from APAReminder import *
import time
import asyncio
import tkinter as tk
from tkinter import ttk
from multiprocessing import dummy as multithreading
import queue

mascot = GUIMascot()
root = mascot.root
style = ttk.Style()
style.theme_use('clam')

rems = []

queue = queue.Queue()

processor = GUIProcessor(root,queue)

rems.append(Reminder(root,"Finish modules",0.2,queue))
rems.append(Reminder(root,"Read textbook",1,queue))

def WorkerThread():
    async def tasks():
        for r in rems:
            asyncio.ensure_future(r.start())
        print("End of tasks")
    loop = asyncio.new_event_loop()
    GUIProcessor.workerLoop = loop
    try:
        loop.run_until_complete(tasks())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

pool = multithreading.Pool(1)
pool.apply_async(WorkerThread)

processor.periodicCall()
root.mainloop()

pool.terminate()
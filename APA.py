from APAGraphics import GUIButton, GUIPrompt, GUIProcessor
from APAReminder import *
import time
import asyncio
import tkinter as tk
from tkinter import ttk
from multiprocessing import dummy as multithreading
import queue

rems = []

queue = queue.Queue()

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

processor = GUIProcessor(root,queue)

rems.append(Reminder(root,"Finish modules",1,queue))
rems.append(Reminder(root,"Read textbook",1,queue))


def WorkerThread():
    async def tasks():
        for r in rems:
            asyncio.ensure_future(r.start())
        print("End of tasks")
    loop = asyncio.new_event_loop()


    try:
        loop.run_until_complete(tasks())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

pool = multithreading.Pool(1)
pool.apply_async(WorkerThread)
GUIProcessor.workerThread = pool

processor.periodicCall()
root.mainloop()

pool.close()
pool.join()
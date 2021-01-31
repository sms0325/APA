from APAGraphics import GUIButton, GUIPrompt
from APAReminder import *
import time
import asyncio

rems = []

rems.append(Reminder("Finish modules",1,"r"))
rems.append(Reminder("Read textbook",1,"r"))

async def main():
    await asyncio.gather(rems[0].start(), rems[1].start())

'''loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()'''

asyncio.run(main())
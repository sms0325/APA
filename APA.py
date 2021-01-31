from APAGraphics import GUIButton, GUIPrompt
from APAReminder import *
import time

rem = Reminder("Work on code", 1,"r")

yes = GUIButton("Yes", lambda: rem.yes())
snz = GUIButton("Snooze", lambda: rem.snz())
gui = GUIPrompt("Hello", yes, snz)
gui.show("hello hello")

time.sleep(2)
gui.show("new prompt")
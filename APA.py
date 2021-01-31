from APAGraphics import GUIButton, GUIPrompt
import time

yes = GUIButton("Yes", lambda: print("yes"))
snz = GUIButton("Snooze", lambda: print("snooze"))
gui = GUIPrompt("Hello", yes, snz)
gui.show("hello hello")

time.sleep(2)
gui.show("new prompt")
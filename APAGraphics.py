import tkinter as tk
from tkinter import ttk
from sys import platform
import random
import math
import queue

class GUIProcessor():
    workerThread = None
    def __init__(self, queue):
        self.queue = queue

    def processIncoming(self):
        while not self.queue.empty():
            func = self.queue.get(0)
            func()

class FloatingWindow():
    def __init__(self, window, grip):
        self.window = window
        self.grip = grip
        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")

class GUIButton():
    def __init__(self, name, func):
        self.name = name
        self.func = func

class GUIPrompt():
    def __init__(self, master, title, confirmBtn : GUIButton, cancelBtn : GUIButton):
        self.master = master
        self.title = title
        self.confirmBtn = confirmBtn
        self.cancelBtn = cancelBtn
        self.root = None

    def confirm(self):
        self.hide()
        GUIProcessor.workerThread.apply_async(self.confirmBtn.func)
    
    def cancel(self):
        self.hide()
        GUIProcessor.workerThread.apply_async(self.cancelBtn.func)

    def show(self, message, mascot = None):
        def createWindow():
            if mascot == None:
                mascot = 'CherryBois/CherryBoi_Surprise.png'
            
            print(platform)
            
            transparentcolor = "#7d7a00"
            if platform == "darwin":
                transparentcolor = 'systemTransparent'

            self.root = tk.Toplevel(self.master)
            self.root.overrideredirect(1)
            self.root.attributes('-topmost', True)
            if platform == "win32":
                self.root.attributes('-transparentcolor', transparentcolor)
            elif platform == "darwin":
                self.root.attributes('-transparent', True)
            self.root.configure(bg=transparentcolor)
            
            cherryBoi = tk.PhotoImage(file=mascot)
            grip = tk.Label(self.root, image=cherryBoi, bg=transparentcolor)
            grip.image = cherryBoi
            grip.pack()

            backgroundColor = "white"
            fontStyle = "Calibri"
            confirmColor = "green"
            cancelColor = "red"

            style = ttk.Style()
            style.configure('Title.TLabel', font=(fontStyle, '18', 'bold'), background=backgroundColor)
            style.configure('Message.TLabel', font=(fontStyle, '13'), background=backgroundColor)
            style.configure('Confirm.TButton', font=(fontStyle, '12'), bordercolor=confirmColor, borderwidth=4, foreground=confirmColor, background=backgroundColor)
            style.map('Confirm.TButton', background=[("active", confirmColor)], foreground=[("active", backgroundColor)], font=[("active", (fontStyle, '12', 'bold'))])
            style.configure('Cancel.TButton', font=(fontStyle, '12'), bordercolor=cancelColor, borderwidth=4, foreground=cancelColor, background=backgroundColor)
            style.map('Cancel.TButton', background=[("active", cancelColor)], foreground=[("active", backgroundColor)], font=[("active", (fontStyle, '12', 'bold'))])

            underMascot = tk.Frame(self.root, bg=backgroundColor, borderwidth=5)
            underMascot.pack(fill=tk.X)
            underMascot.columnconfigure(1, weight=1)
            promptTitle = ttk.Label(underMascot, text=self.title, wraplength=400, justify=tk.LEFT, style='Title.TLabel')
            promptTitle.grid(column=0, columnspan=3, row=0, padx=10)
            promptMessage = ttk.Label(underMascot, text=message, style='Message.TLabel')
            promptMessage.grid(column=0, columnspan=3, row=1, padx=10)
            confirmButton = ttk.Button(underMascot, text=self.confirmBtn.name, command=self.confirm, style='Confirm.TButton')
            confirmButton.grid(column=0, row=3, padx=5)
            cancelButton = ttk.Button(underMascot, text=self.cancelBtn.name, command=self.cancel, style='Cancel.TButton')
            cancelButton.grid(column=2, row=3, padx=5)

            width = self.root.winfo_screenwidth() - math.floor(self.root.winfo_reqwidth() * 2)
            height = self.root.winfo_screenheight() - self.root.winfo_reqheight() - 80
            self.root.geometry(f"+{random.randint(0,width)}+{random.randint(0,height)}")

            FloatingWindow(self.root, grip)
        
        return createWindow
    
    def hide(self):
        self.root.destroy()
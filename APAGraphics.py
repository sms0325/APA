import tkinter as tk
from sys import platform

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
    def __init__(self, name, func, style : dict = {}):
        self.name = name
        self.func = func
        self.style = style

class GUIPrompt():
    def __init__(self, title, confirmBtn : GUIButton, cancelBtn : GUIButton):
        self.title = title
        self.confirmBtn = confirmBtn
        self.cancelBtn = cancelBtn
        self.root = None

    def confirm(self):
        self.hide()
        self.confirmBtn.func()
    
    def cancel(self):
        self.hide()
        self.cancelBtn.func()

    def show(self, message, mascot = None):
        if mascot == None:
            mascot = 'CherryBois/CherryBoi_Surprise.png'
        
        print(platform)
        transparentcolor = "#7d7a00"
        if platform == "darwin":
            transparentcolor = 'systemTransparent'
        self.root = tk.Tk()
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
        
        underMascot = tk.Frame(self.root, bg="white")
        underMascot.pack(fill=tk.X)
        underMascot.columnconfigure(1, weight=1)
        promptTitle = tk.Label(underMascot, text=self.title, bg="white")
        promptTitle.grid(column=0, columnspan=3, row=0)
        promtMessage = tk.Label(underMascot, text=message, bg="white")
        promtMessage.grid(column=0, columnspan=3, row=1)
        confirmButton = tk.Button(underMascot, text=self.confirmBtn.name, command=self.confirm, **self.confirmBtn.style)
        confirmButton.grid(column=0, row=3)
        cancelButton = tk.Button(underMascot, text=self.cancelBtn.name, command=self.cancel, **self.cancelBtn.style)
        cancelButton.grid(column=2, row=3)

        FloatingWindow(self.root, grip)
        self.root.mainloop()
    
    def hide(self):
        self.root.destroy()
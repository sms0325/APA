import tkinter as tk

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


transparentcolor = "#7d7a00"
root = tk.Tk()
# root.overrideredirect(1)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', transparentcolor)
canvas = tk.Canvas(root, width=400, height=200)
canvas.grid(columnspan=3)
canvas.configure(bg=transparentcolor)

cherryBoi = tk.PhotoImage(file='CherryBois/CherryBoi_Surprise.png')
grip = tk.Label(image=cherryBoi, bg=transparentcolor)
grip.image = cherryBoi
grip.grid(column=1, row=0)
FloatingWindow(root, grip)
root.mainloop()


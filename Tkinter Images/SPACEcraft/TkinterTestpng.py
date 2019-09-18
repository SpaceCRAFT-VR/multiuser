from tkinter import *

# pip install pillow
from PIL import Image, ImageTk
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("EXMap1.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Map")
root.geometry("800x800")

root.mainloop()

root = Tk()
def callback(event):
    print ("x-coordinate", event.x,"y-coordinate", event.y)
frame = Frame(root, width=800, height=800)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()

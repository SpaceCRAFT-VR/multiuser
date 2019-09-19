from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

root = Tk()

# Define event based on mouse click
def callback(event):
    print ("x-coordinate", event.x,"y-coordinate", event.y)
canvas = Canvas(root, width = 800, height = 800)      
canvas.bind("<Button-1>", callback)
canvas.pack()

# Render Image on Canvas
img = ImageTk.PhotoImage(Image.open("EXMap1.png"))          
canvas.create_image(0,0, anchor=NW, image=img)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
app = Window(root)
root.wm_title("Map of MSL Curiosity on Sol 157")
root.geometry("800x800")
root.mainloop()

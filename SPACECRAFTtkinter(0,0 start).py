from tkinter import *

# pip install pillow
from PIL import Image, ImageTk



# Define event based on mouse click
def callback(event):
    print ("x-coordinate", event.x,"y-coordinate", event.y) 
    fileCoordinate= open ("Coordinates.txt", "a+")
    L=(event.x, event.y)
    fileCoordinate.write((f'{L}\n'))
    fileCoordinate.close()
    global click_number
    global x1, y1
# Draw line between 2 coordinates from mouse left click
    #if click_number==0:
        #x1=event.x
        #y1=event.y
        #a1, b1 = (event.x - 1), (event.y - 1)
        #a2, b2 = (event.x + 1), (event.y + 1)
        #canvas.create_oval(a1,b1,a2,b2,fill='black',width=10)
        #click_number=1
    #else:
        #x2=event.x
        #y2=event.y
        #a1, b1 = (event.x - 1), (event.y - 1)
        #a2, b2 = (event.x + 1), (event.y + 1)
        #canvas.create_oval(a1,b1,a2,b2,fill='black',width=10)
        #canvas.create_line(x1,y1,x2,y2,fill='black',width=5)
        #click_number=0
# Draw line from origin 0,0 to X,Y (mouse left click)
    x1=0
    y1=0
    x2=event.x
    y2=event.y
    a1, b1 = (event.x - 1), (event.y - 1)
    a2, b2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(a1,b1,a2,b2,fill='black',width=10)     
    canvas.create_line(x1,y1,x2,y2,fill='black',width=5)
         

#def motion(event):
#    x, y = event.x, event.y
#    print('{}, {}'.format(x, y))
#root.bind('<Motion>', motion)
       
root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.bind("<Button-1>", callback)   
click_number=0 #needed for line between 2 coordinates
canvas.pack()

# Render Image on Canvas
img = ImageTk.PhotoImage(Image.open("EXMap1.png"))      
canvas.create_image(0,0,anchor=NW,image=img)
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
       
app = Window(root)
root.wm_title("Map of MSL Curiosity on Sol 157")
root.geometry("800x800")
root.mainloop()

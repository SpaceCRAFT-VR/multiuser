from tkinter import *

# pip install pillow
from PIL import Image, ImageTk



# Define event based on mouse click
def callback(event):
    print ("x-coordinate", event.x,"y-coordinate", event.y)  #Prints the x,y coordinates
    fileCoordinate= open ("Coordinates.txt", "a+")           #Variable set (fileCoordinate) to create a new txt file, 
                                                             #the a+ appends it to the text file
    L=(event.x, event.y)                                     #Variable set (L) to tuple for event.x and event.y
    fileCoordinate.write((f'{L}\n'))                         #.write command writes (L) into the txt file,
                                                             #the f'' inside the .write command makes it a float vs string input
    fileCoordinate.close()                                   #.close command closes the txt file, allowing for appending
    global click_number                                      #so the callback can look for outside variables
    global x1, y1
# (Loop 1) The following draws line between 2 coordinates from mouse left click
# add # in front of lines 21-35 if want a line from 0,0 to click
    if click_number==0: 
        x1=event.x
        y1=event.y
        a1, b1 = (event.x - 1), (event.y - 1)
        a2, b2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(a1,b1,a2,b2,fill='black',width=10)
        click_number=1
    else:
        x2=event.x
        y2=event.y
        a1, b1 = (event.x - 1), (event.y - 1)
        a2, b2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(a1,b1,a2,b2,fill='black',width=10)
        canvas.create_line(x1,y1,x2,y2,fill='black',width=5)
        click_number=0
# (Loop 2) The following draws line from origin 0,0 to X,Y (mouse left click)
# remove # in front of lines 38-45 to get line from 0,0 to click (make sure to add # in front of lines 21-35)
    #x1=0
    #y1=0
    #x2=event.x
    #y2=event.y
    #a1, b1 = (event.x - 1), (event.y - 1)
    #a2, b2 = (event.x + 1), (event.y + 1)
    #canvas.create_oval(a1,b1,a2,b2,fill='black',width=10)     
    #canvas.create_line(x1,y1,x2,y2,fill='black',width=5)
         
       
root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.bind("<Button-1>", callback)   
click_number=0 #needed for line between 2 coordinates
               #This is the initial click number for Loop 1
               #Does not affect Loop 2
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

#Movement and binding keys
from tkinter import *
from time import *

stop = False
timer = int(round(time() * 1000))
s=4
maxspeed = 20
acceleration = 0.5

def moveLeft(event):
    global timer
    global s
    global maxspeed
    global acceleration
    timer2 = timer
    timer = int(round(time() * 1000))
    print(timer,timer2)
    if((timer-timer2)>40):
        s=4
    if s>maxspeed:
        s=maxspeed
    x1,y1 = canvas.coords(bdot)
    x1=x1-(0.5*s)
    #x2=x2-(0.5*s)
    canvas.coords(bdot,x1,y1)
    canvas.update()
    s=s+acceleration
def moveRight(event):
    global timer
    global s
    global acceleration
    global maxspeed
    timer2 = timer
    timer = int(round(time() * 1000))
    print(timer,timer2)
    if((timer-timer2)>40):
        s=4
    if s>maxspeed:
        s=maxspeed
    x1,y1 = canvas.coords(bdot)
    x1=x1+(0.5*s)
    #x2=x2+(0.5*s)
    canvas.coords(bdot,x1,y1)
    canvas.update()
    s=s+acceleration
def moveUp(event):
    global timer
    global s
    global acceleration
    global maxspeed
    timer2 = timer
    timer = int(round(time() * 1000))
    print(timer,timer2)
    if((timer-timer2)>40):
        s=4
    if s>maxspeed:
        s=maxspeed
    x1,y1 = canvas.coords(bdot)
    y1=y1-(0.5*s)
    #y2=y2-(0.5*s)
    canvas.coords(bdot,x1,y1)
    canvas.update()
    s=s+acceleration
def moveDown(event):
    global timer
    global s
    global acceleration
    global maxspeed
    timer2 = timer
    timer = int(round(time() * 1000))
    
    print(timer,timer2)
    if((timer-timer2)>40):
        s=4
    if s>maxspeed:
        s=maxspeed
    x1,y1= canvas.coords(bdot)
    y1=y1+(0.5*s)
    #y2=y2+(0.5*s)
    canvas.coords(bdot,x1,y1)
    canvas.update()
    s=s+acceleration

        
window = Tk()
canvas = Canvas(window, width=800, height=600, bg='white')
thiefImage = PhotoImage(file = 'Thief.png')
bdot = canvas.create_image(100,140,image=thiefImage, anchor = NW)

canvas.pack()
window.bind("<Left>", moveLeft)
window.bind("<Right>", moveRight)
window.bind("<Up>", moveUp)
window.bind("<Down>", moveDown)
window.mainloop()

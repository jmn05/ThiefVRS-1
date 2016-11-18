from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *
from math import *
simulating = False #Boolean flag for when the simulation is running to stop certain functions from running
target = [0,0,0]

window = Tk() #Creates a new tkinter window


#This function fully closes python
def quit():
    global window
    window.quit()
    window.destroy()

#initalises the window
window.title("Thief VRS")
window.geometry("800x600")

controlPanel = Frame(window) # A Frame for all the buttons to go into

#creates a canvas for the virtual robots to move on
C = Canvas(window,height=500,width=800,bg="white")
C.pack()

numberOfTreasures = 8
treasuresList = []

class Treasure():
    location =[]
    def __init__(self):
        self.location = [randrange(0,775),randrange(0,475)]
        image = C.create_oval(self.location[0],self.location[1],self.location[0]+25,self.location[1]+25)
        
photo = PhotoImage(file = "Thief.gif")
    
       
class Thief():
    def __init__(self):
        self.location = [randrange(0,750),randrange(0,450)]
        self.speed = 1
        self.image2 = C.create_image(self.location[0],self.location[1],image=photo, anchor = CENTER)
        self.speed = 1
        self.move = 1
        self.notready = False
    def move_up(self):
        self.location[1] = self.location[1] - self.move*self.speed
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
    def move_down(self):
        self.location[1] = self.location[1] + self.move*self.speed
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
    def move_right(self):
        self.location[0] = self.location[0] + self.move*self.speed
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
    def move_left(self):
        self.location[0] = self.location[0] - self.move*self.speed
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()    
##    def move_up(self):
##        self.location[1] -= self.speed
##    def move_down(self):
##        self.location[1] += self.speed
##    def move_left(self):
##        self.location[0] -= self.speed
##    def move_right(self):
##        self.location[0] += self.speed

for i in range(0,numberOfTreasures):
    treasuresList.append(Treasure())
    print(treasuresList[i].location)

thief = Thief()

def getNearestTreasure():
    global treasuresList
    global thief
    global target
    current = 0
    best = 10000
    for i in range(0,len(treasuresList)):
        print(thief.location[0])
        current = sqrt(((thief.location[0]-treasuresList[i].location[0])**2) + ((thief.location[1]-treasuresList[i].location[1])**2))
        if current < best:
            best = current
            target[0] = int(treasuresList[i].location[0])
            target[1] = int(treasuresList[i].location[1])
            target[2] = i
        print(target[2])


def thiefMove():
    global thief
    global treasuresList
    global target
    getNearestTreasure()
    while thief.location[0] != target[0] and thief.location[1] != target[1]:
        if thief.location[0] < target[0]:
            thief.move_right()
            print("Kupa")
        else:
            thief.move_left()
            print("Hello")
        if thief.location[1] < target[1]:
            thief.move_down()
        else:
            thief.move_up()
    print(target[2])
    treasuresList.pop(target[2])
    getNearestTreasure()
    if len(treasuresList) == 0:
        simulating = False
    else:
        thiefMove()
        
    
    

def resetTreasures():
    global treasuresList
    treasuresList = []
    global numberOfTreasures
    for i in range(0,numberOfTreasures):
        treasuresList.append(Treasure())
        print(treasuresList[i].location)
    
def callReset():
    C.delete("all")
    global treasuresList
    resetTreasures()
    thief = Thief()

def placeThief():
    thief = Thief()

#Gives the buttons their various properties
resetCanvas = Button(controlPanel, text="Reset", command= callReset)
startButton = Button(controlPanel, text = "Start Simulation", command = thiefMove)
stopButton = Button(controlPanel,text = "End Simulation")
quitButton = Button(controlPanel, text = "Quit", command= quit)

#Places the button on the screen
controlPanel.pack()
resetCanvas.pack(side=LEFT)
startButton.pack(side=LEFT)
stopButton.pack(side=LEFT)
quitButton.pack(side=LEFT)



################################################################################################################

def mainLoop():
    global treasuresList
    global thief
    getNearestTreasure()
    window.after(mainLoop(),16)
    

#window.after(mainLoop(),16)

window.mainloop()

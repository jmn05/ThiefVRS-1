from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *
from math import *
simulating = False #Boolean flag for when the simulation is running to stop certain functions from running
target = [0,0]

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
        image2 = C.create_image(self.location[0],self.location[1],image=photo, anchor = NW)
    def move_up(self):
        self.location[1] -= self.speed
    def move_down(self):
        self.location[1] += self.speed
    def move_left(self):
        self.location[0] -= self.speed
    def move_right(self):
        self.location[0] += self.speed

for i in range(0,numberOfTreasures):
    treasuresList.append(Treasure())
    print(treasuresList[i].location)

thief = Thief()

def startSimulation():
    global simulating
    simulating = True
    window.after(16,mainLoop())
 
def stopSimulation():
    global simulating
    simulating = False

    
def getNearestTreasure():
    global treasuresList
    global thief
    global target
    current = 0
    best = 10000
    for i in range(0,len(treasuresList)):
        current = sqrt(((thief.location[0]-treasuresList[i].location[0])**2) + ((thief.location[1]-treasuresList[i].location[1])**2))
        if current < best:
            target[0] = int(treasuresList[i].location[0])
            target[1] = int(treasuresList[i].location[1])
    print(target)


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
startButton = Button(controlPanel, text = "Start Simulation",command=startSimulation)
quitButton = Button(controlPanel, text = "Quit", command= quit)

#Places the button on the screen
controlPanel.pack()
resetCanvas.pack(side=LEFT)
startButton.pack(side=LEFT)
quitButton.pack(side=LEFT)



################################################################################################################

def mainLoop():
    global treasuresList
    global thief
    global simulating
    while simulating == True:
        getNearestTreasure()
        
    
    

window.after(16,mainLoop())

window.mainloop()

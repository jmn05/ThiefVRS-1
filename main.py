from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *
from math import *
simulating = False #Boolean flag for when the simulation is running to stop certain functions from running
target = [0,0]
score = 0

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

photo = PhotoImage(file = "Thief.gif")
photo2 = PhotoImage(file = "cop.gif")
photo3 = PhotoImage(file = "coin.gif")
photo4 = PhotoImage(file = "cop.gif")
class Back():
#Gives the buttons their various properties
    def __init__(self):
        self.location = [randrange(0,725),randrange(0,425)]
        image5 = C.create_image(self.location[0],self.location[1],image=photo4, anchor = NW)

class Treasure():
    location =[]
    def __init__(self):
        self.location = [randrange(0,725),randrange(0,425)]
        image4 = C.create_image(self.location[0],self.location[1],image=photo3, anchor = NW)
        


class Thief():
    def __init__(self):
        self.location = [randrange(0,725),randrange(0,425)]
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

class Cop():
    def __init__(self):
        self.location = [randrange(0,725),randrange(0,425)]
        self.speed = 1
        image3 = C.create_image(self.location[0],self.location[1],image=photo2, anchor = NW)

for i in range(0,numberOfTreasures):
    treasuresList.append(Treasure())
    print(treasuresList[i].location)

thief = Thief()
cop = Cop()
back = Back ()

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
            target[0] = int(treasuresList[i].location[0])
            target[1] = int(treasuresList[i].location[1])
        print(best)


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
    cop = Cop()



#Gives the buttons their various properties
resetCanvas = Button(controlPanel, text="Reset", command= callReset)
startButton = Button(controlPanel, text = "Start Simulation")
stopButton = Button(controlPanel,text = "End Simulation")
quitButton = Button(controlPanel, text = "Quit", command= quit)
scoreLabel = Label(controlPanel, text="Score: " + str(score))

#Places the button on the screen
controlPanel.pack()
resetCanvas.pack(side=LEFT)
startButton.pack(side=LEFT)
stopButton.pack(side=LEFT)
quitButton.pack(side=LEFT)
scoreLabel.pack()



################################################################################################################

def mainLoop():
    global treasuresList
    global thief
    getNearestTreasure()
    window.after(mainLoop(),16)
    

#window.after(mainLoop(),16)

window.mainloop()

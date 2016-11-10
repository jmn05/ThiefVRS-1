from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *

simulating = False #Boolean flag for when the simulation is running to stop certain functions from running

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

class treasure():
    location =[]
    def __init__(self):
        self.location = [randrange(0,775),randrange(0,475)]
        image = C.create_oval(self.location[0],self.location[1],self.location[0]+25,self.location[1]+25)
        

    
        
class thief:
    xspeed = 0
    yspeed = 0
    locations = {}

treasuresList = []

for i in range(0,numberOfTreasures):
    treasuresList.append(treasure())
    print(treasuresList[i].location)

def resetTreasures():
    global treasuresList
    global numberOfTreasures
    
    for i in range(0,numberOfTreasures):
        treasuresList.append(treasure())
        print(treasuresList[i].location)
    
def callReset():
    C.delete("all")
    global treasuresList
    resetTreasures()


#Gives the buttons their various properties
placeThiefButton = Button(controlPanel, text = "Place Thief")
placeCopButton = Button(controlPanel, text = "Place Cops")
placeTreasuresButton = Button(controlPanel, text = "Place Treasures", command=callReset)
startButton = Button(controlPanel, text = "Start Simulation")
stopButton = Button(controlPanel,text = "End Simulation")
quitButton = Button(controlPanel, text = "Quit", command= quit)

#Places the button on the screen
controlPanel.pack()
placeThiefButton.pack(side=LEFT)
placeCopButton.pack(side=LEFT)
placeTreasuresButton.pack(side=LEFT)
startButton.pack(side=LEFT)
stopButton.pack(side=LEFT)
quitButton.pack(side=LEFT)



################################################################################################################





window.mainloop()



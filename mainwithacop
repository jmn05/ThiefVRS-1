from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *
import math

simulating = False #Boolean flag for when the simulation is running to stop certain functions from running

window = Tk() #Creates a new tkinter window

#This function fully closes python
def quit():
    window.quit()
    window.destroy()

#initalises the window
window.title("Thief VRS")
window.geometry("800x600")

controlPanel = Frame(window) # A Frame for all the buttons to go into

#creates a canvas for the virtual robots to move on
C = Canvas(window,height=500,width=800,bg="gray")
C.pack()

global numberOfTreasures
global treasuresList
numberOfTreasures = 8
treasuresList = []

class Treasure():
    location =[]
    def __init__(self):
        self.location = [randrange(0,725),randrange(0,425)]
        image = C.create_oval(self.location[0],self.location[1],self.location[0]+25,self.location[1]+25)
        
photo = PhotoImage(file = "Thief.gif")
photocop = PhotoImage(file = "cop.gif")

class Thief():
    def __init__(self):
        self.location = [randrange(50,750),randrange(50,550)]
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
        self.location = [randrange(50,750),randrange(50,550)]
        self.speed = 1
        self.move = 0.8
        self.notready = False
        self.copObj = C.create_image(self.location[0],self.location[1],image=photocop, anchor = CENTER)
    def move_up(self):
        self.location[1] = self.location[1] - self.move*self.speed
        C.coords(self.copObj,self.location[0],self.location[1])
        C.update()
    def move_down(self):
        self.location[1] = self.location[1] + self.move*self.speed
        C.coords(self.copObj,self.location[0],self.location[1])
        C.update()
    def move_right(self):
        self.location[0] = self.location[0] + self.move*self.speed
        C.coords(self.copObj,self.location[0],self.location[1])
        C.update()
    def move_left(self):
        self.location[0] = self.location[0] - self.move*self.speed
        C.coords(self.copObj,self.location[0],self.location[1])
        C.update()
    def move_random(self):
        self.ranlocation = [randrange(25,775),randrange(25,575)]
        self.notready=True
        while(self.notready):
            if(self.ranlocation[0] > self.location[0]):
                self.move_right()
            if(self.ranlocation[0] < self.location[0]):
                self.move_left()
            if(self.ranlocation[1] > self.location[1]):
                 self.move_down()
            if(self.ranlocation[1] < self.location[1]):
                 self.move_up()
            if(math.fabs(round(self.location[0]) - self.ranlocation[0])<=1 and math.fabs(round(self.location[1]) - self.ranlocation[1])<=1):
                self.notready=False
            print(self.location, "TO", self.ranlocation)
    def movemove(self):
        while(True):
            if(self.notready==False):
                self.move_random()
            
cop = Cop()
Thief()
for i in range(0,numberOfTreasures):
    treasuresList.append(Treasure())

def resetTreasures():
    treasuresList = []
    Thief()
    for i in range(0,numberOfTreasures):
        treasuresList.append(Treasure())
       


def callReset():
    C.delete("all")
    resetTreasures()
    

def placeThief():
    Thief()

def placeCop():
    Cop()

#Gives the buttons their various properties
resetCanvas = Button(controlPanel, text="Reset", command= callReset)
startButton = Button(controlPanel, text = "Start Simulation")
stopButton = Button(controlPanel,text = "End Simulation")
quitButton = Button(controlPanel, text = "Quit", command= quit)
cop.movemove()
#Places the button on the screen
controlPanel.pack()
resetCanvas.pack(side=LEFT)
startButton.pack(side=LEFT)
stopButton.pack(side=LEFT)
quitButton.pack(side=LEFT)



################################################################################################################





window.mainloop()

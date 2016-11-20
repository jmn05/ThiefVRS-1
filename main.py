from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *
from math import *
simulating = False #Boolean flag for when the simulation is running to stop certain functions from running
target = [0,0,0]
count = 0
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

#import of the file containing the thief image        
photo = PhotoImage(file = "Thief.gif")
photo2 = PhotoImage(file = "coin.gif")


#defines the class treasure
class Treasure():
    global location
    def __init__(self):
        self.location = [randrange(0,775),randrange(0,475)]
        self.image = C.create_image(self.location[0],self.location[1],image=photo2, anchor = CENTER)   

#defines the class thief and all the movements the thief can make       
class Thief():
    def __init__(self):
        self.location = [randrange(0,750),randrange(0,450)]
        self.image2 = C.create_image(self.location[0],self.location[1],image=photo, anchor = CENTER)
        self.speed = 5
        self.move = 1
        self.notready = False
    def move_up(self):
        self.location[1] = self.location[1] - self.move*self.speed
        if self.location[1] < target[1]:
            self.location[1] = target[1]
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
    def move_down(self):
        self.location[1] = self.location[1] + self.move*self.speed
        if self.location[1] > target[1]:
            self.location[1] = target[1]
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
    def move_right(self):
        self.location[0] = self.location[0] + self.move*self.speed
        if self.location[0] > target[0]:
            self.location[0] = target[0]
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
    def move_left(self):
        self.location[0] = self.location[0] - self.move*self.speed
        if self.location[0] < target[0]:
            self.location[0] = target[0]
        C.coords(self.image2,self.location[0],self.location[1])
        C.update()
        
thief = Thief()

#this function gets the nearest treasure based on the thief location
def getNearestTreasure():
    global treasuresList
    global thief
    global target
    best = 1000
    for i in range(0,len(treasuresList)):
        current = sqrt(((thief.location[0]-treasuresList[i].location[0])**2) + ((thief.location[1]-treasuresList[i].location[1])**2))
        if current < best:
            best = current
            target[0] = int(treasuresList[i].location[0])
            target[1] = int(treasuresList[i].location[1])
            target[2] = int(i)
        print(target[2])

#this function moves the thief to the closest treasure and catches it
def thiefMove():
    global thief
    global treasuresList
    global target
    global count
    while len(treasuresList) != 0:
        getNearestTreasure()
        while thief.location[0] != target[0] or thief.location[1] != target[1]:
            if thief.location[0] < target[0]:
                thief.move_right()
            else:
                thief.move_left()
            if thief.location[1] < target[1]:
                thief.move_down()
            else:
                thief.move_up()
        C.delete(treasuresList.pop(int(target[2])).image)
        print("couves")
        
#this function deletes all the treasures and sets new random treasures
def resetTreasures():
    global treasuresList
    treasuresList = []
    global numberOfTreasures
    for i in range(0,numberOfTreasures):
        treasuresList.append(Treasure())
        print(treasuresList[i].location)

#this function clears the canvas and calls the functions responsible to create new treasures, a new thief and a new cop   
def callReset():
    C.delete("all")
    global treasuresList
    resetTreasures()
    thief = Thief()

#this function places a thief into the canvas
def placeThief():
    thief = Thief()

for i in range(0,numberOfTreasures):
    treasuresList.append(Treasure())
    print(treasuresList[i].location)

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
    window.after(mainLoop(),16)
    

#window.after(mainLoop(),16)

window.mainloop()

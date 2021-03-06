from tkinter import * #Imports tkinter for the GUI
from time import * #Times is used for animations
from random import *
from math import *
import math
import time
import random

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

background_image= PhotoImage(file = "background.gif")
C.create_image(400,300,image=background_image, anchor = CENTER)

numberOfTreasures = 8
treasuresList = []

#import of the file containing the thief image        
photo = PhotoImage(file = "Thief.gif")
photo2 = PhotoImage(file = "coin.gif")
copImage = PhotoImage(file="cop.gif")
copImageLeft = PhotoImage(file="cop2.gif")

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
        self.speed = 1
        self.move = 0.2
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

class Cop():
    def __init__(self):
        self.location = [600,60]
        self.copO = C.create_image(self.location[0],self.location[1],image=copImage,anchor=CENTER)
    # SETUP
    direction = 360 #angle
    speed = 0.2
    ready=True
    found=False
    def goTow(self):
        if(self.direction in [90,180]):
            goX=0
            goY = math.sin(math.radians(self.direction))
        elif(self.direction in [240,360]):
            goX = math.cos(math.radians(self.direction))
            goY = 0
        else:
            goX = math.cos(math.radians(self.direction))
            goY = math.sin(math.radians(self.direction))
        self.location = [self.location[0]+(goX*self.speed),self.location[1]+(goY*self.speed)]
        C.coords(self.copO,self.location[0],self.location[1])
        C.update()
    def dirGen(self, tarX, tarY):
        #print("X:",tarX,"Y:",tarY)
        x= self.location[0]
        y= self.location[1]
        vecX = math.fabs(tarX - self.location[0])
        vecY = math.fabs(tarY - self.location[1])
        if(x<tarX and y<tarY):
            self.direction = 90-math.degrees(math.atan(vecY/vecX))  
        elif(x>tarX and y>tarY):
            self.direction = 180+(90-math.degrees(math.atan(vecY/vecX)))
        elif(x>tarX and y<tarY):
            self.direction = 90+(90-math.degrees(math.atan(vecY/vecX)))
        elif(x<tarX and y>tarY):
            self.direction = 240+(90-math.degrees(math.atan(vecY/vecX)))
        elif(x==tarX and y>tarY):
            self.direction = 90
        elif(x==tarX and y<tarY):
            self.direction = 270
        elif(x<tarX and y==tarY):
            self.direction = 360
        elif(x>tarX and y==tarY):
            self.direction = 180
       # print(math.degrees(math.atan(vecY/vecX)))
        return True
    def goTo(self, TargetX, TargetY):
        tarX = random.randrange(50,750)
        tarY = random.randrange(50,550)

        self.ready=False
        if(math.sqrt((self.location[0]-TargetX)**2 + (self.location[1]-TargetY)**2)<100):
            if(math.fabs(round(self.location[0]-TargetX))<1 and math.fabs(round(self.location[1]-TargetY)<1)):
                self.found=True
            self.speed=0.3
            self.dirGen(TargetX,TargetY)
            self.goTow()
            
        self.dirGen(tarX,tarY)
       # if(self.direction>90 and self.direction<240):
        #    C.itemconfig(self.copO, image=copImageLeft)
       # else:
        #    C.itemconfig(self.copO, image=copImage)
        self.goTow()
        if(math.fabs(round(self.location[0]-tarX))<1 and math.fabs(round(self.location[1]-tarY)<1)):
            self.ready = True
        return True
                
        #print(self.location)
    def start(self, tarX, tarY):
       # if(self.ready):
        self.goTo(tarX, tarY)
        #if(self.found == True):
           # C.delete(Target)



thief = Thief()
cop = Cop()

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
killloop = False
print(killloop)
def thiefMove():
    global thief
    global treasuresList
    global target
    global count
    global killloop
    while(len(treasuresList) != 0):
        if(killloop):
            break
            
        getNearestTreasure()
        while(thief.location[0] != target[0] or thief.location[1] != target[1]):
            if(killloop):
                break
            if thief.location[0] < target[0]:
                thief.move_right()
                cop.start(thief.location[0], thief.location[1])
                
            else:
                thief.move_left()
                cop.start(thief.location[0], thief.location[1])
                
            if thief.location[1] < target[1]:
                thief.move_down()
                cop.start(thief.location[0], thief.location[1])

            else:
                thief.move_up()
                cop.start(thief.location[0], thief.location[1])
                
        C.delete(treasuresList.pop(int(target[2])).image)
        count = count +1
        updateScore()

def Movement():
    global killloop
    global scoreText
    killloop = False
    scoreText = C.create_text(0,0,anchor = NW, text = str("0"))
    thiefMove()
    
def updateScore():
    global count
    scoreText = 0
    C.delete("scoreText")
    C.create_text(10, 10, text = str(count), tag = "scoreText")

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
    global killloop
    global treasuresList
    global thief
    global cop
    
    C.delete("all")
    killloop=True
    C.create_image(400,300,image=background_image, anchor = CENTER)
    resetTreasures()
    thief = Thief()
    cop = Cop()

for i in range(0,numberOfTreasures):
    treasuresList.append(Treasure())
    print(treasuresList[i].location)

#Gives the buttons their various properties
resetCanvas = Button(controlPanel, text="Reset", command= callReset)
startButton = Button(controlPanel, text = "Start Simulation", command = Movement)
quitButton = Button(controlPanel, text = "Quit", command= quit)

#Places the button on the screen
controlPanel.pack()
resetCanvas.pack(side=LEFT)
startButton.pack(side=LEFT)
quitButton.pack(side=LEFT)


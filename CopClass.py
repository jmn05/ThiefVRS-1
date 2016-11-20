from tkinter import *
import math
import time
import random

window = Tk() #creates a new tkinter window

C = Canvas(window, width=800, height=600) # Canvas :)
C.pack()

copImage = PhotoImage(file="cop.gif")
copImageLeft = PhotoImage(file="cop2.gif")
thief = PhotoImage(file="thief.gif")

#TargetX and TargetY are used in class
TargetX = 300 #Thief X
TargetY = 500 #Thief Y
Target = C.create_image(TargetX,TargetY,image=thief,anchor=CENTER) #Thief Object

class Cop():
    def __init__(self):
        self.location = [600,60] # Start location
        self.copO = C.create_image(self.location[0],self.location[1],image=copImage,anchor=CENTER)
    # SETUP !!!!!! DON'T CHANGE ANYTHING HERE
    direction = 360 #angle
    speed = 0.05
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
    def goTo(self):
        tarX = random.randrange(50,750) #Random location X
        tarY = random.randrange(50,550) #Random location X
        while(True):
            self.ready=False
            if(math.sqrt((self.location[0]-TargetX)**2 + (self.location[1]-TargetY)**2)<100):
                if(math.fabs(round(self.location[0]-TargetX))<1 and math.fabs(round(self.location[1]-TargetY)<1)):
                    self.found=True
                    break
                self.speed=0.1 #Goes faster when sees a thief
                self.dirGen(TargetX,TargetY) #Target location, change it for thief location
                self.goTow()
                continue
            
            self.dirGen(tarX,tarY)
            if(self.direction>90 and self.direction<240):
                C.itemconfig(self.copO, image=copImageLeft)
            else:
                C.itemconfig(self.copO, image=copImage)
            self.goTow()
            if(math.fabs(round(self.location[0]-tarX))<1 and math.fabs(round(self.location[1]-tarY)<1)):
                self.ready = True
                break
        return True
    def start(self):
        if(self.ready):
            self.goTo()
        if(self.found == False):
            self.start()
        else:
            C.delete(Target)
            
copObj = Cop()         
copObj.start()
window.mainloop()

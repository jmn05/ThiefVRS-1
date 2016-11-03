from tkinter import * #Imports tkinter for the GUI

simulating = False #Boolean flag for when the simulation is running to stop certain functions from running

window = tkinter.Tk() #Creates a new tkinter window

#This function fully closes python
def quit():
    global window
    window.quit()
    window.destroy()

#initalises the window
window.title("Thief VRS")
window.geometry("800x600")

controlPanel = Frame(window) # A Frame for all the buttons to go into

#Gives the buttons their various properties
placeThiefButton = Button(controlPanel, text = "Place Thief")
placeCopButton = Button(controlPanel, text = "Place Cop")
startButton = Button(controlPanel, text = "Start Simulation")
stopButton = Button(controlPanel,text = "End Simulation")
quitButton = Button(controlPanel, text = "Quit", command= quit)

#Places the button on the screen
controlPanel.pack()
placeThiefButton.pack(side=LEFT)
placeCopButton.pack(side=LEFT)
startButton.pack(side=LEFT)
stopButton.pack(side=LEFT)
quitButton.pack(side=LEFT)


#creates a canvas for the virtual robots to move on
C = Canvas(window,height=500,width=800,bg="white")
C.pack()

window.mainloop()




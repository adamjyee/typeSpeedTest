#importing all libraries
from os import close
import random, tkinter


#open the text file with words in
def getWords():
    #declares tuple var as list so it can be appended to
    words200Tuple = []
    #opens text file with all words
    words200 = open("200words1line.txt", "r")
    #reads from file and changes it into a string, and then a list
    words200Tuple = (str((words200.readline()))).split()
    #changes to a tuple so things wont be messed with
    words200Tuple = tuple(words200Tuple)
    words200.close()
    return(words200Tuple)


#creates a random list of the the tuple read from the file in the func above
#this is unfortunately made into a global but because it's immutable it's not as bad
def wordGenerator(wordTuple):
    randomWordTuple = []
    for x in range(300):
        randomWordTuple.append(wordTuple[random.randint(0,(len(wordTuple)-1))])
    tuple(randomWordTuple)
    return randomWordTuple


#a function for when the user chooses to start the test
def run():
    print("the test would be starting")


#a test function to output when a key has been pressed
#has to have arg event otherwise outputs an error
#the key that has been pressed is in the char part of the "event" var (can be called with keysym)
def keyPress(event):
    print("a key has been pressed")
    #returns the key that's been pressed
    return(event.keysym)


#this is the equivalent of the main function, it makes the app and uses mainloop() to run
#
def app():
    print("running app")
    #initialising the tkinter interpreter (would be done anyway after the first widget, but useful)
    root= tkinter.Tk()

    #creates the canvas
    app = tkinter.Canvas(root, width = 400, height = 300)
    app.pack()

    typeBox = tkinter.Entry (root)
    app.create_window(200, 140, window=typeBox)

    #shows the first few words for test, taken from the getWords function
    text1 = tkinter.Label(root, fg="green", text= randomWords[0:8])

    #a declaration of where the text is in the window
    app.create_window(200, 100, window= text1)

    #a button
    startButton = tkinter.Button(root, text='Start typing test', command= run)
    #a declaration of where the button is in the window
    app.create_window(200, 180, window= startButton)

    #a check to find if a key has been pressed (doesnt work yet)
    #used website https://www.python-course.eu/tkinter_events_binds.php
    typeBox.bind('<Key>', keyPress)

    root.mainloop()

randomWords = tuple(wordGenerator(getWords()))
app()

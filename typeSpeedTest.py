#importing all libraries
from os import close
import random, tkinter, time

def start():
    saveFile = open("saveFile","a")
    saveFile.writelines("\nstart time="+str(time.time()))

#open the text file with words in
def getWords():
    #declares tuple var as list so it can be appended to
    words200Tuple = []
    #opens text file with all words
    words200 = open("200words1line.txt", "r")
    #reads and 
    words200Tuple = str((words200.readline())).split()
    words200Tuple = tuple(words200Tuple)
    words200.close()
    return(words200Tuple)


def wordGenerator(wordTuple):
    return wordTuple[random.randint(0,len(wordTuple))]


#a function for when the user chooses to start the test
def run():
    #this all happens after the start test button is pressed
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(60)
    print("finished")
    


#a test function to output when a key has been pressed
#has to have arg event otherwise outputs an error
#the key that has been pressed is in the char part of the "event" var
def keyPress(event):
    print("a key has been pressed")
    #adds the keypress to the save file
    saveFile("key",event.keysym)
    #returns the key that's been pressed
    return(event.keysym)


def saveFile(fileType, data):
    saveFile = open("saveFile","a")
    if fileType == "key":
        saveFile.write(","+str(data))


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
    text1 = tkinter.Label(root, text= getWords()[0:8])
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

start()
app()

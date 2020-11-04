#importing all libraries
from os import close
import random, tkinter



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


#a function for when the user chooses to start the test
def run():
    print("the test would be starting")


def window():
    #initialising the tkinter interpreter (would be done anyway after the first widget, but useful)
    root= tkinter.Tk()

    #creates the canvas
    window = tkinter.Canvas(root, width = 400, height = 300)
    window.pack()

    typeBox = tkinter.Entry (root)
    window.create_window(200, 140, window=typeBox)

    #taking the input from the typebox
    userInput = typeBox.get()


    #some text on the window
    text1 = tkinter.Label(root, text= userInput)
    #a declaration of where the text is in the window
    window.create_window(200, 100, window=text1)

    #a button
    button = tkinter.Button(text='Start typing test', command=run)
    #a declaration of where the button is in the window
    window.create_window(200, 180, window=button)
    root.mainloop()

window()
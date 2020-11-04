#importing all libraries
import random, tkinter

#initialising the tkinter interpreter (would be done anyway after the first widget, but useful)
root= tkinter.Tk()

#creates the canvas
window = tkinter.Canvas(root, width = 400, height = 300)
window.pack()

typeBox = tkinter.Entry (root)
window.create_window(200, 140, window=typeBox)

#taking the input from the typebox
userInput = typeBox.get()


#a function for when the user chooses to start the test
def start():
    pass


#some text on the window
text1 = tkinter.Label(root, text= userInput)
#a declaration of where the text is in the window
window.create_window(200, 230, window=text1)

#a button
button = tkinter.Button(text='Start typing test', command=start)
#a declaration of where the button is in the window
window.create_window(200, 180, window=button)

root.mainloop()
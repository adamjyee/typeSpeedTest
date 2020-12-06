#importing all libraries
from os import close
import random, tkinter as tk, time, pickle

def rewriteCountFile():
    with open("pickledCount", "wb") as countFile:
        pickle.dump(0, countFile)

def start():
    try:
        saveFile = open("saveFile","a")
        try:
            saveFile.writelines("\nstart time="+str(time.time()))
            saveFile.writelines("\nkeys pressed: \n")
            saveFile.close
            #https://stackoverflow.com/questions/35090264/what-is-the-best-way-to-save-tuples-in-python used this here and in all other instances of pickling
            with open("pickleSaveFile", "wb") as pickleSave:
                pickle.dump(createWordList(), pickleSave)
        except OSError:
            print("file handling error 2")
    except OSError:
        print("file handling error 1")


#open the text file with words in
def getWords():
    #declares tuple var as list so it can be appended to
    words200Tuple = []
    #opens text file with all words
    words200 = open("200words1line.txt", "r")
    #reads and makes the file into a tuple, so it cannot be changed.
    words200Tuple = str((words200.readline())).split()
    words200Tuple = tuple(words200Tuple)
    words200.close()
    return(words200Tuple)


def wordGenerator(wordTuple):
    return wordTuple[random.randint(0,(len(wordTuple)-1))]


def createWordList():
    wordTuple = getWords()
    list = []
    for x in range(300):
        list.append(wordGenerator(wordTuple))
    return tuple(list)


#a function for when the user chooses to start the test
def run():
    #this all happens after the start test button is pressed
    print("3")
    #count down from 1
    print("2")
    #count down 1
    print("1")
    #count down from 60
    print("finished")


class App():
    def __init__(self, *args, **kwargs):
        self.root = root
        self.wordsOnScreen = 12
        print("running init func")
        self.previousCount = 0
        self.spaceCount = 0


    def createApp(self):
        print("running app")
        with open("pickleSaveFile","rb") as pickleFile:
            self.fullRandomWordTuple = pickle.load(pickleFile)
        print(len(self.fullRandomWordTuple))


        #creates the canvas
        self.applicationWindow = tk.Canvas(root, width = 400, height = 300)
        self.applicationWindow.pack()

        self.typeBox = tk.Entry (root)
        self.applicationWindow.create_window(200, 140, window=self.typeBox)

        
        #shows the first few words for test, taken from the getWords function
        self.text1 = tk.Label(root, text=(self.fullRandomWordTuple)[0:self.wordsOnScreen])
        #a declaration of where the text is in the window
        self.applicationWindow.create_window(200, 100, window= self.text1)

        #a button
        self.startButton = tk.Button(root, text='Start typing test', command= run)
        #a declaration of where the button is in the window
        self.applicationWindow.create_window(200, 180, window= self.startButton)

        #a check to find if a key has been pressed (doesnt work yet)
        #used website https://www.python-course.eu/tkinter_events_binds.php
        self.typeBox.bind("<BackSpace>",self.backspaceFunc)
        self.typeBox.bind("<space>", self.spaceFunc)
        self.typeBox.bind("<Key>", keyPress)


    def changeText(self):
        pass


#called when the user types a space char
    def spaceFunc(self,event):
        self.clearEntryBox(event)
        self.spaceCount += 1
        print(self.spaceCount)
        saveFile = open("saveFile","a")
        saveFile.write("\n")
        saveFile.close


#this is called by the space func method to clear the text box once the user has finished typing the word
    def clearEntryBox(self,event):
        self.typeBox.delete("0","end")


#the function that is called when backspace is pressed
    def backspaceFunc(self, event):
        #this is to declare the final line as a string
        updatedFinalLine = ""
        #opens save file
        with open("saveFile", "r") as saveFile:
            #reads all and saves as var
            saveFileContent = (saveFile.readlines())
        saveFile.close
        #takes the final line from the savefile list
        updatedFinalLineList = ((saveFileContent[-1]).split())[:-1]
        #then changes the list back to a string with spaces in between
        for char in range(len(updatedFinalLineList)):
            updatedFinalLine = (str(updatedFinalLine) + str(updatedFinalLineList[char]) + " ")
        #updates the var with the new line
        saveFileContent[-1] = updatedFinalLine
        #writes to the file
        with open("saveFile","w") as saveFile:
            for line in saveFileContent:
                saveFile.write("%s" % line)
        #calls the function to reduce the count by one
        subtractCount(event)


    #getters
    def getWordsOnScreen(self):
        return self.wordsOnScreen
    def getPreviousCount(self):
        return self.previousCount



#a test function to output when a key has been pressed
#has to have arg event otherwise outputs an error
#the key that has been pressed is in the char part of the "event" var
def keyPress(event):
    print("a key has been pressed")
    #adds the keypress to the save file using the savefile function
    #this function also calls the check keypress function which checks if the user has correctly entered the next key
    saveFile("key",event.keysym)
    #returns the key that's been pressed
    checkKeyPress(event.keysym)
    return(event.keysym)


def saveFile(fileType, data):
    saveFile = open("saveFile","a")
    #if char = backspace then count - 1
    if fileType == "key" and (len(data) == 1):
        saveFile.write(str(data)+" ")
        with open("pickledCount", "rb") as countFile:
            count = pickle.load(countFile)
        countFile.close
        count += 1
        print("count = "+str(count))
        with open("pickledCount","wb") as countFile:
            pickle.dump(count, countFile)
    return(data)


#function called by keypress to compare between the key that's been pressed and the word tuple
def checkKeyPress(data):
    with open("pickleSaveFile", "rb") as tupleFile:
        FullRandomWordTuple = pickle.load(tupleFile)
    with open("pickledCount", "rb") as countFile:
        count = pickle.load(countFile)
    #this is a list that has all the words as just characters
    #this allows me to search for the specific letter in the sequence
    allCharList = []
    for x in range(len(FullRandomWordTuple)):
        for i in range(len(FullRandomWordTuple[x])):
            allCharList.append((list(FullRandomWordTuple[x]))[i])

    #if the user has typed the correct char
    #moving to when the user presses space
    if data == allCharList[count]:
        pass
    #if the user has typed the wrong char
    else:
        pass

#function used to subtract one from the "count"
#unpickles the number, does the calculation, pickles the number
def subtractCount(event):
    #unpickling
    with open("pickledCount", "rb") as countFile:
        count = pickle.load(countFile)
    countFile.close
    #check so it doesnt go negative
    if count > 0:
        count -= 1
    #debugging (delete)
    print("count = "+str(count))
    #repickles
    with open("pickledCount","wb") as countFile:
        pickle.dump(count, countFile)


if __name__ == "__main__":
    #initialising the tk interpreter (would be done anyway after the first widget, but useful)
    root = tk.Tk()
    rewriteCountFile()
    start()
    #used this https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
    App().createApp()
    root.mainloop()

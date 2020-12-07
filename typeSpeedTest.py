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


class App():
    def __init__(self,root):
        print("running init func")
        self.root = root
        self.wordsOnScreen = 12
        self.previousCount = 0
        self.spaceCount = 0
        self.correctChar = 0
        self.startTime = 0
        self.testRunning = bool
        self.timeForTest = 3
        self.cpm = 0
        self.testRan = False


    def createApp(self):
        print("running app")
        with open("pickleSaveFile","rb") as pickleFile:
            self.fullRandomWordTuple = pickle.load(pickleFile)
        print(len(self.fullRandomWordTuple))

        #creates the canvas
        self.applicationWindow = tk.Canvas(self.root, width = 400, height = 300)
        self.applicationWindow.pack()

        self.typeBox = tk.Entry (self.root)
        self.applicationWindow.create_window(200, 140, window=self.typeBox)
        
        #shows the first few words for test, taken from the getWords function
        self.typeText = tk.Label(self.root, text=(self.fullRandomWordTuple)[0:self.wordsOnScreen])
        #a declaration of where the text is in the window
        self.applicationWindow.create_window(200, 100, window= self.typeText)

        self.countdownText = tk.Label(self.root, text=("press the button to start"))
        self. applicationWindow.create_window(200, 75, window= self.countdownText)

        #a button
        self.startButton = tk.Button(self.root, text='Start typing test', command= self.startTest)
        #a declaration of where the button is in the window
        self.applicationWindow.create_window(200, 180, window= self.startButton)

        #a check to find if a key has been pressed (doesnt work yet)
        #used website https://www.python-course.eu/tkinter_events_binds.php
        self.typeBox.bind("<BackSpace>",self.backspaceFunc)
        self.typeBox.bind("<space>", self.spaceFunc)
        self.typeBox.bind("<Key>", self.keyPress)

        self.checkTime()


    def checkTime(self):
        if not(self.testRan and not(self.testRunning) == True ):
            self.root.after(100,self.checkTime)
            if self.testRunning == True:
                print(time.time() - self.startTime)
            try:
                if (self.startTime < time.time() - self.timeForTest) and self.testRan == True:
                    print("test finished")
                    self.endTest()
            except:
                pass 


    def changeTypeText(self,startNum):
        self.typeText.configure(text= (self.fullRandomWordTuple[startNum:startNum+self.wordsOnScreen]))
        self.typeText.update()


#called when the user types a space char
    def spaceFunc(self,event):
        if self.testRunning == True:
            self.clearEntryBox()
            self.checkWord()
            self.spaceCount += 1
            if self.spaceCount%self.wordsOnScreen == 0:
                self.changeTypeText(self.spaceCount)
            saveFile = open("saveFile","a")
            saveFile.write("\n")
            saveFile.close

    
    def checkWord(self):
        recentWord = ""
        with open("saveFile", "r") as saveFile:
            saveFileContents = saveFile.readlines()
            for char in range(len((saveFileContents[-1].split()))):
                recentWord = (recentWord + saveFileContents[-1].split()[char])
        if recentWord == self.fullRandomWordTuple[self.spaceCount]:
            self.correctChar += len(recentWord)
        print("correct = "+ str(self.correctChar))


#this is called by the space func method to clear the text box once the user has finished typing the word
    def clearEntryBox(self):
        self.typeBox.delete("0","end")


#the function that is called when backspace is pressed
    def backspaceFunc(self, event):
        if self.testRunning == True:
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

    
    def startTest(self):
        
        self.clearEntryBox()
        self.countdownText.configure(text= "3")
        self.countdownText.update()
        time.sleep(1)
        self.countdownText.configure(text= "2")
        self.countdownText.update()
        time.sleep(1)
        self.countdownText.configure(text= "1")
        self.countdownText.update()
        time.sleep(1)
        self.countdownText.configure(text= "go!")
        self.testRunning = True
        self.startTime = time.time()
        self.spaceCount = 0
        self.testRan = True

    def endTest(self):
        self.testRunning = False
        self.cpm = self.correctChar/(self.timeForTest/60)
        try:
            #this deletes the buttons from the window
            print("destroying")
            self.startButton.destroy()
            self.typeBox.destroy()
            self.typeText.destroy()
        except:
            print("destroy method failed")
        try:
            saveFile = open("saveFile","r")
            if ["c","p","m"] != list(saveFile.readlines()[-1])[:3]:
                saveFile = open("saveFile", "a")
                saveFile.write("cpm = "+str(self.cpm))
                print("adding cpm")
                #creates the object to show the wpm
                self.cpmText = tk.Label(self.root, text=("CPM = "+str(self.cpm)))
                #a declaration of where the text is in the window
                self.applicationWindow.create_window(200, 100, window= self.cpmText)
                #creates the object to show the wpm
                self.wpmText = tk.Label(self.root, text=("WPM = "+str(self.cpm/5)))
                #tells the wpm label to be below the cpm label
                self.applicationWindow.create_window(200, 150, window=self.wpmText)
        except:
            print("saveFile has been deleted")


    #getters
    def getWordsOnScreen(self):
        return self.wordsOnScreen
    def getPreviousCount(self):
        return self.previousCount
    def gettestRunningVar(self):
        return self.testRunning


    #a test function to output when a key has been pressed
    #has to have arg event otherwise outputs an error
    #the key that has been pressed is in the char part of the "event" var
    def keyPress(self,event):
        if self.gettestRunningVar() == True:
            print("a key has been pressed")
            #adds the keypress to the save file using the savefile function
            #this function also calls the check keypress function which checks if the user has correctly entered the next key
            saveFile("key",event.keysym)
            #returns the key that's been pressed
            return(event.keysym)
        else:
            print("press the start button to start")

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


def main():
    #initialising the tk interpreter (would be done anyway after the first widget, but useful)
    root = tk.Tk()
    rewriteCountFile()
    start()
    #used this https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
    App(root).createApp()
    root.mainloop()

if __name__ == "__main__":
    main()
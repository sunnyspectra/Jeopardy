import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("500x500")
root.title('CS Jeopardy!')
root.resizable(False, False)

endOfGameFrame = tk.Frame(root, bg="#00008b", padx=5, pady=5)
endOfGameFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)
question = tk.Frame(root, bg="#00008b", padx=5, pady=5)
question.place(x=0, y=0, relwidth=1.0, relheight=1.0)
board = tk.Frame(root, bg="#00008b", padx=5, pady=5)
board.place(x=0, y=0, relwidth=1.0, relheight=1.0)
endScreenLabel=tk.Label(endOfGameFrame, text="Thanks for \n playing \n CS Jeopardy!",font=("Courier", 50, "bold"))
endScreenLabel.pack()

score=0

def endOfGame():
    if(questionsAnswered==20):
        endOfGameFrame.tkraise()
    else:
        global board
        board.tkraise()


# configure the grid
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=0)


continueButton=tk.Button(question, text="Press to continue",command=endOfGame)  #button to press in order to go back to board

questionsAnswered=0

        

def twoChoices():                       #setup a question that has only two answer choices
    question.tkraise()                  #raise the question frame
    aButton.place(x=200, y=425)
    bButton.place(x=250, y=425)
    cButton.place_forget()              #hide the options that do not apply
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def threeChoices():                     #setup a question that has only three answer choices
    question.tkraise()
    aButton.place(x=175, y=425)
    bButton.place(x=225, y=425)
    cButton.place(x=275, y=425)
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def fourChoices():                      #setup a question that has only four answer choices
    question.tkraise()
    aButton.place(x=150, y=425)
    bButton.place(x=200, y=425)
    cButton.place(x=250, y=425)
    dButton.place(x=300, y=425)
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def fiveChoices():                      #setup a question that has only five answer choices
    question.tkraise()
    aButton.place(x=125, y=425)
    bButton.place(x=175, y=425)
    cButton.place(x=225, y=425)
    dButton.place(x=275, y=425)
    eButton.place(x=325, y=425)
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def sixChoices():                       #setup a question that has only six answer choices
    question.tkraise()
    aButton.place(x=100, y=425)
    bButton.place(x=150, y=425)
    cButton.place(x=200, y=425)
    dButton.place(x=250, y=425)
    eButton.place(x=300, y=425)
    fButton.place(x=350, y=425)
    gButton.place_forget()
    hButton.place_forget()
def sevenChoices():                     #setup a question that has only seven answer choices
    question.tkraise()
    aButton.place(x=75, y=425)
    bButton.place(x=125, y=425)
    cButton.place(x=175, y=425)
    dButton.place(x=225, y=425)
    eButton.place(x=275, y=425)
    fButton.place(x=325, y=425)
    gButton.place(x=375, y=425)
    hButton.place_forget()
def eightChoices():                     #setup a question that has only eight answer choices
    question.tkraise()
    aButton.place(x=50, y=425)
    bButton.place(x=100, y=425)
    cButton.place(x=150, y=425)
    dButton.place(x=200, y=425)
    eButton.place(x=250, y=425)
    fButton.place(x=300, y=425)
    gButton.place(x=350, y=425)
    hButton.place(x=400, y=425)


aButton = tk.Button(question, text="a")     #setup buttons for multiple choice
bButton =tk.Button(question,text="b")
cButton =tk.Button(question,text="c")
dButton =tk.Button(question,text="d")
eButton=tk.Button(question,text="e")
fButton = tk.Button(question, text="f")
gButton =tk.Button(question,text="g")
hButton =tk.Button(question,text="h")
correctOrWrong=tk.Label(question,text="")   #label that says if player is right or wrong
correctOrWrong.pack(side=tk.TOP)            #place label on top



def rightAnswer():                          #What to do when you get an answer right
    correctOrWrong.configure(text=" Correct ")  #tell player that they are correct
    aButton.place_forget()
    bButton.place_forget()
    cButton.place_forget()
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
    continueButton.place(x=175,y=425)       #place the continue button to go back to board
    global questionsAnswered
    questionsAnswered=questionsAnswered+1   #increase number of questions answered
    
def wrongAnswer():                          #What do do when you get an answer wrong
    correctOrWrong.configure(text="Incorrect")  #tel player they are incorrect
    aButton.place_forget()
    bButton.place_forget()
    cButton.place_forget()
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
    continueButton.place(x=175,y=425)
    global questionsAnswered
    questionsAnswered=questionsAnswered+1   #increase number of questions answered
def rightAnswerA():                         #When A is the right answer
    aButton.config(command=rightAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerB():                         #When B is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=rightAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerC():                         #When C is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=rightAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerD():                         #When D is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=rightAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerE():                         #When E is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=rightAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerF():                         #When F is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=rightAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerG():                         #When G is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=rightAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerH():                         #When H is the right answer
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=rightAnswer)


#prep images for each questions

img01 = tk.PhotoImage(file="IfElse200.png")
img01_fit = img01.subsample(2)
img02 = tk.PhotoImage(file="IfElse400.png")
img02_fit = img02.subsample(2)
img03 = tk.PhotoImage(file="IfElse600.png")
img03_fit = img03.subsample(2)
img04 = tk.PhotoImage(file="IfElse800.png")
img04_fit = img04.subsample(2)
img05 = tk.PhotoImage(file="IfElse1000.png")
img05_fit = img05.subsample(2)
img06 = tk.PhotoImage(file="while200.png")
img06_fit = img06.subsample(2)
img07 = tk.PhotoImage(file="while400.png")
img07_fit = img07.subsample(2)
img08 = tk.PhotoImage(file="while600.png")
img08_fit = img08.subsample(2)
img09 = tk.PhotoImage(file="while800.png")
img09_fit = img09.subsample(2)
img10 = tk.PhotoImage(file="while1000.png")
img10_fit = img10.subsample(2)
img11 = tk.PhotoImage(file="ListsAndCollections200.png")
img11_fit = img11.subsample(2)
img12 = tk.PhotoImage(file="ListsAndCollections400.png")
img12_fit = img12.subsample(2)
img13 = tk.PhotoImage(file="ListsAndCollections600.png")
img13_fit = img13.subsample(2)
img14 = tk.PhotoImage(file="ListsAndCollections800.png")
img14_fit = img14.subsample(2)
img15 = tk.PhotoImage(file="ListsAndCollections1000.png")
img15_fit = img15.subsample(2)
img16 = tk.PhotoImage(file="functions200.png")
img16_fit = img16.subsample(2)
img17 = tk.PhotoImage(file="functions400.png")
img17_fit = img17.subsample(2)
img18 = tk.PhotoImage(file="functions600.png")
img18_fit = img18.subsample(2)
img19 = tk.PhotoImage(file="functions800.png")
img19_fit = img19.subsample(2)
img20 = tk.PhotoImage(file="functions1000.png")
img20_fit = img20.subsample(3)



pictureLabel = tk.Label(question, font = "50") #create picture label to put images on
pictureLabel.pack()



#IfElse Loops
def ifElseStat200():                    #command for respective name
    correctOrWrong.config(text="")      #reset label that shows if player is correct
    continueButton.place_forget()       #hide the continue button
    question.tkraise()                  #raise the question frame
    pictureLabel.configure(image=img01_fit) #set the image to the respecting picture
    fourChoices()                       #number of choices for problem
    rightAnswerD()                      #what the answer is for the problem
    ifElse200.grid_forget()             #remove the button from the board
def ifElseStat400():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img02_fit)
    fiveChoices()
    rightAnswerC()
    ifElse400.grid_forget()
def ifElseStat600():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img03_fit)
    sevenChoices()
    rightAnswerB()
    ifElse600.grid_forget()
def ifElseStat800():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img04_fit)
    twoChoices()
    rightAnswerB()
    ifElse800.grid_forget()
def ifElseStat1000():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img05_fit)
    eightChoices()
    rightAnswerD()
    ifElse1000.grid_forget()
#while loops
def while200():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img06_fit)
    twoChoices()
    rightAnswerB()
    whileLoop200.grid_forget()
def while400():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img07_fit)
    fourChoices()
    rightAnswerC()
    whileLoop400.grid_forget()
def while600():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img08_fit)
    fiveChoices()
    rightAnswerE()
    whileLoop600.grid_forget()
def while800():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img09_fit)
    fiveChoices()
    rightAnswerB()
    whileLoop800.grid_forget()
def while1000():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img10_fit)
    fiveChoices()
    rightAnswerC()
    whileLoop1000.grid_forget()
#lists and collections
def listsAndCollect200():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img11_fit)
    threeChoices()
    rightAnswerA()
    ListsAndCollections200.grid_forget()
def listsAndCollect400():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img12_fit)
    sixChoices()
    rightAnswerB()
    ListsAndCollections400.grid_forget()
def listsAndCollect600():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img13_fit)
    threeChoices()
    rightAnswerA()
    ListsAndCollections600.grid_forget()
def listsAndCollect800():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img14_fit)
    eightChoices()
    rightAnswerB()
    ListsAndCollections800.grid_forget()
def listsAndCollect1000():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img15_fit)
    sixChoices()
    rightAnswerB()
    ListsAndCollections1000.grid_forget()
#functions
def function200():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img16_fit)
    sixChoices()
    rightAnswerF()
    Functions200.grid_forget()
def function400():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img17_fit)
    twoChoices()
    rightAnswerB()
    Functions400.grid_forget()
def function600():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img18_fit)
    twoChoices()
    rightAnswerA()
    Functions600.grid_forget()
def function800():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img19_fit)
    fourChoices()
    rightAnswerD()
    Functions800.grid_forget()
def function1000():
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img20_fit)
    sixChoices()
    rightAnswerE()
    Functions1000.grid_forget()



ifElseLabel=tk.Label(board, text="If-Else \n Statements").grid(row=0,column=0)      #create a label to show the category name
ifElse200=tk.Button(board,text="200",height = 2, width = 6,bg = "#073763", fg="#ffd700", command=ifElseStat200)   #create button for specific question
ifElse200.grid(row=1,column=0,padx=10,pady=5)                                       #place into grid
ifElse400=tk.Button(board,text="400",height = 2, width = 6,bg = "#073763", fg="#ffd700", command=ifElseStat400)
ifElse400.grid(row=2,column=0,padx=10,pady=5)
ifElse600=tk.Button(board,text="600",height = 2, width = 6,bg = "#073763", fg="#ffd700", command=ifElseStat600)
ifElse600.grid(row=3,column=0,padx=10,pady=5)
ifElse800=tk.Button(board,text="800",height = 2, width = 6,bg = "#073763", fg="#ffd700", command=ifElseStat800)
ifElse800.grid(row=4,column=0,padx=10,pady=5)
ifElse1000=tk.Button(board,text="1000",height = 2, width = 6,bg = "#073763", fg="#ffd700", command=ifElseStat1000)
ifElse1000.grid(row=5,column=0,padx=10,pady=5)

whileLabel=tk.Label(board,text="While \n Loops").grid(row=0,column=1,padx=10,pady=5)
whileLoop200=tk.Button(board,text="200",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=while200)
whileLoop200.grid(row=1,column=1,padx=10,pady=5)
whileLoop400=tk.Button(board,text="400",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=while400)
whileLoop400.grid(row=2,column=1,padx=10,pady=5)
whileLoop600=tk.Button(board,text="600",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=while600)
whileLoop600.grid(row=3,column=1,padx=10,pady=5)
whileLoop800=tk.Button(board,text="800",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=while800)
whileLoop800.grid(row=4,column=1,padx=10,pady=5)
whileLoop1000=tk.Button(board,text="1000",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=while1000)
whileLoop1000.grid(row=5,column=1,padx=10,pady=5)

ListsAndCollectionsLabel=tk.Label(board,text="List and \n Collections").grid(row=0,column=2,padx=10,pady=5)
ListsAndCollections200=tk.Button(board,text="200",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=listsAndCollect200)
ListsAndCollections200.grid(row=1,column=2,padx=10,pady=5)
ListsAndCollections400=tk.Button(board,text="400",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=listsAndCollect400)
ListsAndCollections400.grid(row=2,column=2,padx=10,pady=5)
ListsAndCollections600=tk.Button(board,text="600",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=listsAndCollect600)
ListsAndCollections600.grid(row=3,column=2,padx=10,pady=5)
ListsAndCollections800=tk.Button(board,text="800",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=listsAndCollect800)
ListsAndCollections800.grid(row=4,column=2,padx=10,pady=5)
ListsAndCollections1000=tk.Button(board,text="1000",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=listsAndCollect1000)
ListsAndCollections1000.grid(row=5,column=2,padx=10,pady=5)

FunctionsLabel=tk.Label(board,text="Functions").grid(row=0,column=3,padx=10,pady=5)
Functions200=tk.Button(board,text="200",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=function200)
Functions200.grid(row=1,column=3,padx=10,pady=5)
Functions400=tk.Button(board,text="400",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=function400)
Functions400.grid(row=2,column=3,padx=10,pady=5)
Functions600=tk.Button(board,text="600",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=function600)
Functions600.grid(row=3,column=3,padx=10,pady=5)
Functions800=tk.Button(board,text="800",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=function800)
Functions800.grid(row=4,column=3,padx=10,pady=5)
Functions1000=tk.Button(board,text="1000",height = 2, width = 6,bg = "#073763",fg="#ffd700", command=function1000)
Functions1000.grid(row=5,column=3,padx=10,pady=5)


root.mainloop()

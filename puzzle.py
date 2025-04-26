import random
import time
from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("Puzzle Game")
root.configure(background="Cadet Blue")

Tops = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial', 80, 'bold'), text="Advanced Puzzle Game", bd=10, bg="Cadet Blue",
                 fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg="Powder Blue", bd=10, width=1350, height=700, relief=RIDGE)
MainFrame.grid(row=1, column=0, padx=30)

LeftFrame = Frame(MainFrame, bd=10, width=700, height=500, pady=2, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=540, height=500, padx=1, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=540, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2a = Frame(RightFrame, bd=10, width=540, height=140, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2a.grid(row=1, column=0)

RightFrame2b = Frame(RightFrame, bd=10, width=540, height=140, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2b.grid(row=2, column=0)

numberOfClicks = 0
displayClicks = StringVar()
displayClicks.set("Number of Clicks" + "\n" + "0")

gameStateString = StringVar()


def upDateCounter():
    global numberOfClicks, displayClicks
    displayClicks.set("Number of Clicks" + "\n" + str(numberOfClicks))


def gameStateUpdate(gameState):
    global gameStateString
    gameStateString.set(gameState)


class Button_:
    def __init__(self, text, x, y):
        self.enterValue = text
        self.textTaken = StringVar()
        self.textTaken.set(text)
        self.x = x
        self.y = y
        self.btnNumber = Button(LeftFrame, textvariable=self.textTaken, font=('arial', 80), bd=3,
                                command=lambda i=self.x, j=self.y: emptySpotChecker(i, j))
        self.btnNumber.place(x=self.x * 150, y=self.y * 150, width=170, height=170)


def shuffle():
    global btnNumbers, numberOfClicks
    nums = []
    for x in range(12):
        x += 1
        if x == 12:
            nums.append("")
        else:
            nums.append(str(x))

    for y in range(len(btnNumbers)):
        for x in range(len(btnNumbers[y])):
            num = random.choice(nums)
            btnNumbers[y][x].textTaken.set(num)
            nums.remove(num)
    numberOfClicks = 0
    upDateCounter()
    gameStateUpdate("")


lblDisplayClicks = Label(RightFrame1, textvariable=displayClicks, font=('arial', 40)).place(x=0, y=10, width=480,
                                                                                         height=160)
btnShuffle = Button(RightFrame2a, text="New Game", font=('arial', 40), bd=5, command=shuffle).place(x=0, y=10, width=480,
                                                                                                 height=100)

lblDisplayClicks = Label(RightFrame2b, textvariable=gameStateString, font=('arial', 40)).place(x=0, y=10, width=480,
                                                                                         height=100)

btnNumbers = []

name = 0

for y in range(3):
    btnNumbers_ = []
    for x in range(4):
        name += 1
        if name == 12:
            name = ""
        btnNumbers_.append(Button_(str(name), x, y))
    btnNumbers.append(btnNumbers_)

shuffle()


def emptySpotChecker(y, x):
    global btnNumbers, numberOfClicks

    if not btnNumbers[x][y].textTaken.get() == "":
        for i in range(-1, 2):
            newX = x + i

            if not (newX < 0 or len(btnNumbers) - 1 < newX or i == 0):
                if btnNumbers[newX][y].textTaken.get() == "":
                    text = btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[newX][y].textTaken.get())
                    btnNumbers[newX][y].textTaken.set(text)
                    winCheck()
                    break

        for j in range(-1, 2):
            newY = y + j

            if not (newY < 0 or len(btnNumbers[0]) - 1 < newY or j == 0):
                if btnNumbers[x][newY].textTaken.get() == "":
                    text = btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[x][newY].textTaken.get())
                    btnNumbers[x][newY].textTaken.set(text)
                    winCheck()
                    break
        numberOfClicks += 1
        upDateCounter()


def winCheck():
    lost = False
    for y in range(len(btnNumbers)):
        for x in range(len(btnNumbers[y])):
            if btnNumbers[y][x].enterValue != btnNumbers[y][x].textTaken.get():
                lost = True
                break
    if not lost:
        gameStateUpdate("You are a Winner!")

root.mainloop()

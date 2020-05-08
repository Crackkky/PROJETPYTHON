import tkinter as tk

from Projet.View.StyleInterface import *


class TrainingView(tk.Frame):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        tk.Frame.__init__(self, master)
        rootStyle(master)
        self.width = WIDTH
        self.height = HEIGHT
        self.checkPlateList = []
        self.checkPlateVar = []
        self.checkOperatorList = []
        self.checkOperatorVar = []
        self.createWidgets(checkPlateNumber, checkOperatorNumber, master)

    def createWidgets(self, checkPlateNumber, checkOperatorNumber, master):

        self.frameInformation = tk.Frame(master)
        self.checkPlateNumber = checkPlateNumber
        frameStyle(self.frameInformation)

        self.infoLabel = tk.Label(self.frameInformation)
        labelStyle(self.infoLabel)
        self.infoLabel.pack()

        frameButton = tk.Frame(master)
        frameStyle(frameButton)
        frameButton.pack(side=tk.BOTTOM)

        self.validateButton = tk.Button(frameButton)
        buttonStyle(self.validateButton)
        self.validateButton.pack(side='left')

        self.returnButton = tk.Button(master)
        buttonStyle(self.returnButton)
        self.returnButton.place(x=0, y=self.height-self.returnButton.winfo_reqheight())

        self.backButton = tk.Button(frameButton)
        buttonStyle(self.backButton)
        self.backButton.pack(side='right')

        self.newButton = tk.Button(master)
        buttonStyle(self.newButton)
        self.newButton.place(x=self.width-62, y=self.height-28)

        self.solutionButton = tk.Button(master)
        buttonStyle(self.solutionButton)
        self.solutionButton.place(x=self.width - 62, y=self.height - 56)

        frameGoal = tk.Frame(master)
        frameStyle(frameGoal)
        frameGoal.place(x=0, y=0, height=48, width=68)

        self.goalLabel = tk.Label(frameGoal)
        labelStyle(self.goalLabel)
        self.goalLabel.pack(fill='both', expand=5)

        framePlate = tk.Frame(master)
        frameStyle(framePlate)
        framePlate.pack(side=tk.TOP)

        frameOperator = tk.Frame(master)
        frameStyle(frameOperator)
        frameOperator.pack(side=tk.LEFT)

        frameHistory = tk.Frame(master)
        frameStyle(frameHistory)
        self.historyLabel = tk.Label(frameHistory)
        labelStyle(self.historyLabel)
        self.historyLabel.pack(fill='both', expand=5)
        frameHistory.place(x=self.width-65, y=0)

        #init des checks buttons des plaques
        for i in range(0,self.checkPlateNumber) :
            checkButton = tk.Checkbutton(framePlate, indicatoron=0, width = 5)
            checkButton.pack(side='left')
            self.checkPlateList.append(checkButton)
            var = tk.IntVar()
            self.checkPlateVar.append(var)
            checkButton["variable"] = var
            checkButtonStyle(checkButton)

        #init des checks buttons des operators
        for i in range(0, checkOperatorNumber) :
            checkButton = tk.Checkbutton(frameOperator, indicatoron=0,  width = 5)
            checkButton.pack(side='top')
            self.checkOperatorList.append(checkButton)
            var = tk.IntVar()
            self.checkOperatorVar.append(var)
            checkButton["variable"] = var
            checkButtonStyle(checkButton)

    def displayInfo(self, text=None):
        if text == None :
            self.frameInformation.place_forget()
        else :
            self.infoLabel["text"] = text
            self.frameInformation.place(x=150, y=100)

    def showHidePlateButton(self, i, show):
        if show :
            self.checkPlateList[i].pack(side='left')
        else :
            self.checkPlateList[i].pack_forget()

    def showAllPlateButtons(self):
        for i in range(self.checkPlateNumber):
            self.showHidePlateButton(i, 1)
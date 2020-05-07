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
        frameHistory.pack(side=tk.RIGHT)

        self.historyLabel = tk.Label(frameHistory)
        labelStyle(self.historyLabel)
        self.historyLabel.pack(fill='both', expand=5)

        #init des checks buttons des plaques
        for i in range(0,checkPlateNumber) :
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

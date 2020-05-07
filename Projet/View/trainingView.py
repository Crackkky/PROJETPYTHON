import tkinter as tk

from Projet.View.StyleInterface import *


class TrainingView(tk.Frame):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        self.checkPlateList = []
        self.checkPlateVar = []
        self.checkOperatorList = []
        self.checkOperatorVar = []
        self.createWidgets(checkPlateNumber, checkOperatorNumber, master)

    def createWidgets(self, checkPlateNumber, checkOperatorNumber, master):
        rootStyle(master)

        frameButton = tk.Frame(master)
        frameStyle(frameButton)
        frameButton.pack(side=tk.BOTTOM)

        self.validateButton = tk.Button(frameButton)
        self.validateButton.pack(side='left')
        buttonStyle(self.validateButton)

        self.backButton = tk.Button(frameButton)
        self.backButton.pack(side='right')
        buttonStyle(self.backButton)

        frameGoal = tk.Frame(master)
        frameStyle(frameGoal)
        frameGoal.place(x=0, y=0, height=48, width=68)

        self.goalLabel = tk.Label(frameGoal)
        self.goalLabel.pack(fill='both', expand=5)
        labelStyle(self.goalLabel)

        framePlate = tk.Frame(master)
        frameStyle(framePlate)
        framePlate.pack(side=tk.TOP)

        frameOperator = tk.Frame(master)
        frameStyle(frameOperator)
        frameOperator.pack(side=tk.LEFT)

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

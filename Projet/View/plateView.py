import tkinter as tk

from Projet.View.styleInterface import *


class PlateView(tk.Frame):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):

        self.frameInformation = None
        self.checkPlateNumber = None
        self.infoLabel = None
        self.validateButton = None
        self.goalLabel = None
        self.frameButton = None
        self.framePlate = None
        self.frameOperator = None
        self.frameGoal = None
        self.returnButton = None


        tk.Frame.__init__(self, master)
        rootStyle(master)
        self.width = WIDTH
        self.height = HEIGHT
        self.checkPlateList = []
        self.checkPlateVar = []
        self.checkOperatorList = []
        self.checkOperatorVar = []
        self.createPlateView(checkPlateNumber, checkOperatorNumber, master)

    def createPlateView(self, checkPlateNumber, checkOperatorNumber, master):

        self.frameInformation = tk.Frame(master)
        self.checkPlateNumber = checkPlateNumber
        frameStyle(self.frameInformation)

        self.infoLabel = tk.Label(self.frameInformation)
        labelStyle(self.infoLabel)
        self.infoLabel.pack()

        self.frameButton = tk.Frame(master)
        frameStyle(self.frameButton)

        self.validateButton = tk.Button(self.frameButton)
        buttonStyle(self.validateButton)
        self.validateButton.pack(side='left')

        self.frameGoal = tk.Frame(master)
        frameStyle(self.frameGoal)

        self.goalLabel = tk.Label(self.frameGoal)
        labelStyle(self.goalLabel)
        self.goalLabel.pack(fill='both', expand=5)

        self.framePlate = tk.Frame(master)
        frameStyle(self.framePlate)

        self.frameOperator = tk.Frame(master)
        frameStyle(self.frameOperator)

        self.returnButton = tk.Button(master)
        buttonStyle(self.returnButton)

        # afficher à l'écran les données
        self.hideShowGame(1)

        # init des checks buttons des plaques
        for i in range(0, self.checkPlateNumber):
            checkButton = tk.Checkbutton(self.framePlate, indicatoron=0, width=5)
            checkButton.pack(side='left')
            self.checkPlateList.append(checkButton)
            var = tk.IntVar()
            self.checkPlateVar.append(var)
            checkButton["variable"] = var
            checkButtonStyle(checkButton)

        # init des checks buttons des operators
        for i in range(0, checkOperatorNumber):
            checkButton = tk.Checkbutton(self.frameOperator, indicatoron=0, width=5)
            checkButton.pack(side='top')
            self.checkOperatorList.append(checkButton)
            var = tk.IntVar()
            self.checkOperatorVar.append(var)
            checkButton["variable"] = var
            checkButtonStyle(checkButton)

    def displayInfo(self, text=None):
        if text is None:
            self.frameInformation.place_forget()
        else:
            self.infoLabel["text"] = text
            self.frameInformation.place(x=150, y=100)

    def showHidePlateButton(self, i, show):
        if show:
            self.checkPlateList[i].pack(side='left')
        else:
            self.checkPlateList[i].pack_forget()

    def showHideAllPlateButtons(self, show):
        for i in range(self.checkPlateNumber):
            self.showHidePlateButton(i, show)

    def hideShowGame(self, show):
        if show:
            self.frameButton.pack(side=tk.BOTTOM)
            self.frameGoal.place(x=0, y=0, height=53, width=71)
            self.framePlate.pack(side=tk.TOP)
            self.frameOperator.pack(side=tk.LEFT)
            self.returnButton.place(x=0, y=self.height - self.returnButton.winfo_reqheight())

        else:
            self.frameGoal.place_forget()
            self.framePlate.pack_forget()
            self.frameOperator.pack_forget()
            self.frameButton.pack_forget()
            self.returnButton.place_forget()

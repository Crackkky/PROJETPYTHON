import tkinter as tk

from Projet.View.styleInterface import *


class TileView(tk.Frame):
    def __init__(self, checkTileNumber, checkOperatorNumber, master=None):

        self.frameInformation = None
        self.checkTileNumber = None
        self.infoLabel = None
        self.validateButton = None
        self.goalLabel = None
        self.frameButton = None
        self.frameTile = None
        self.frameOperator = None
        self.frameGoal = None
        self.returnButton = None


        tk.Frame.__init__(self, master)
        rootStyle(master)
        self.width = WIDTH
        self.height = HEIGHT
        self.checkTileList = []
        self.checkTileVar = []
        self.checkOperatorList = []
        self.checkOperatorVar = []
        self.createTileView(checkTileNumber, checkOperatorNumber, master)

    def createTileView(self, checkTileNumber, checkOperatorNumber, master):

        self.frameInformation = tk.Frame(master)
        self.checkTileNumber = checkTileNumber
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

        self.frameTile = tk.Frame(master)
        frameStyle(self.frameTile)

        self.frameOperator = tk.Frame(master)
        frameStyle(self.frameOperator)

        self.returnButton = tk.Button(master)
        buttonStyle(self.returnButton)

        # init des checks buttons des plaques
        for i in range(0, self.checkTileNumber):
            checkButton = tk.Checkbutton(self.frameTile, indicatoron=0, width=5)
            checkButton.pack(side='left')
            self.checkTileList.append(checkButton)
            var = tk.IntVar()
            self.checkTileVar.append(var)
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

    def showHideTileButton(self, i, show):
        if show:
            self.checkTileList[i].pack(side='left')
        else:
            self.checkTileList[i].pack_forget()

    def showHideAllTileButtons(self, show):
        for i in range(self.checkTileNumber):
            self.showHideTileButton(i, show)

    def hideShowGame(self, show):
        self.hideShowValidate(show)
        if show:
            self.frameGoal.place(x=0, y=0, height=53, width=71)
            self.frameTile.pack(side=tk.TOP)
            self.frameOperator.pack(side=tk.LEFT)

        else:
            self.frameGoal.place_forget()
            self.frameTile.pack_forget()
            self.frameOperator.pack_forget()
        self.showHideAllTileButtons(show)
        self.hideShowReturnButton(show)

    def hideShowValidate(self, show):
        if show:
            self.frameButton.pack(side=tk.BOTTOM)
        else:
            self.frameButton.pack_forget()

    def hideShowReturnButton(self, show):
        if show:
            self.returnButton.place(x=0, y=self.height - self.returnButton.winfo_reqheight())
        else:
            self.returnButton.place_forget()
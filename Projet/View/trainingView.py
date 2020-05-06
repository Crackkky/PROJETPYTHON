import tkinter as tk

from Projet.View.StyleInterface import buttonStyle, buttonStyleOnArray, frameStyle, rootStyle


class TrainingView(tk.Frame):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        self.checkPlateList = []
        self.checkPlateVar = []
        self.checkOperatorList = []
        self.checkOperatorVar = []
        self.createWidgets(checkPlateNumber, checkOperatorNumber, master)

    def createWidgets(self, checkPlateNumber, checkOperatorNumber, master):
        rootStyle(master)
        self.validateButton = tk.Button(master)
        self.validateButton.pack(side='bottom')
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
            buttonStyle(checkButton)

        #init des checks buttons des operators
        for i in range(0, checkOperatorNumber) :
            checkButton = tk.Checkbutton(frameOperator, indicatoron=0,  width = 5)
            checkButton.pack(side='top')
            self.checkOperatorList.append(checkButton)
            var = tk.IntVar()
            self.checkOperatorVar.append(var)
            checkButton["variable"] = var
            buttonStyle(checkButton)

        buttonStyle(self.validateButton)

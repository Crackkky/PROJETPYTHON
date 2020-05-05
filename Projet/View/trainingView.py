import tkinter as tk


class TrainingView(tk.Frame):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        tk.Frame.__init__(self, master)
        self.checkPlateList = []
        self.checkPlateVar = []
        self.checkOperatorList = []
        self.checkOperatorVar = []
        self.createWidgets(checkPlateNumber, checkOperatorNumber, master)

    def createWidgets(self, checkPlateNumber, checkOperatorNumber, master):
        master.geometry('500x500')
        framePlate = tk.Frame(master, borderwidth=10, background='pink')
        framePlate.pack(side=tk.TOP)
        frameOperator = tk.Frame(master, borderwidth=10, background='pink')
        frameOperator.pack(side=tk.LEFT)
        #init des checks buttons des plaques
        for i in range(0,checkPlateNumber) :
            checkButton = tk.Checkbutton(framePlate, indicatoron=0, activeforeground='gray')
            checkButton.pack(side='left')
            self.checkPlateList.append(checkButton)
            var = tk.IntVar()
            self.checkPlateVar.append(var)
            checkButton["variable"] = var

        #init des checks buttons des operators
        for i in range(0, checkOperatorNumber) :
            checkButton = tk.Checkbutton(frameOperator, indicatoron=0, activeforeground='gray')
            checkButton.pack(side='top')
            self.checkOperatorList.append(checkButton)
            var = tk.IntVar()
            self.checkOperatorVar.append(var)
            checkButton["variable"] = var



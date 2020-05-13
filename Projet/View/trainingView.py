import tkinter as tk

from Projet.View.plateView import PlateView
from Projet.View.StyleInterface import *


class TrainingView(PlateView):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        super(TrainingView, self).__init__(checkPlateNumber, checkOperatorNumber, master)

        self.returnButton = None
        self.newButton = None
        self.solutionButton = None
        self.historyLabel = None
        self.frameHistory = None

        self.createTrainingView(master)

    def createTrainingView(self, master):
        self.returnButton = tk.Button(master)
        buttonStyle(self.returnButton)
        self.returnButton.place(x=0, y=self.height - self.returnButton.winfo_reqheight())

        self.newButton = tk.Button(master)
        buttonStyle(self.newButton)
        self.newButton.place(x=self.width - 62, y=self.height - 28)

        self.solutionButton = tk.Button(master)
        buttonStyle(self.solutionButton)
        self.solutionButton.place(x=self.width - 62, y=self.height - 56)

        self.frameHistory = tk.Frame(master)
        frameStyle(self.frameHistory)
        self.historyLabel = tk.Label(self.frameHistory)
        labelStyle(self.historyLabel)
        self.historyLabel.pack(fill='both', expand=5)
        self.frameHistory.place(x=self.width - 70, y=0, width=70)

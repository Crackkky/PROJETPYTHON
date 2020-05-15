import tkinter as tk
from tkinter import *

from Projet.Controller.connectionMaker import ConnectionMaker
from Projet.Controller.onlineController import OnlineController
from Projet.Controller.trainingController import TrainingController
from Projet.View.mainView import MainView


class MainController :
    def __init__(self, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER):

        self.operators = OPERATORS
        self.operator_number = OPERATOR_NUMBER
        self.plate_number = PLATE_NUMBER

        self.mainView = MainView(root)
        self.mainView.label['text'] = '블랙핑크 하우스 환영합니!'
        texts_button = ["Play in Training", "Play as Online", "Quit"]
        buttonsPosition = [self.mainView.trainingButton, self.mainView.onlineButton, self.mainView.quitButton]
        fcts = [lambda : self.trainingMode(root), lambda :self.onlineMode(root), lambda :sys.exit()]
        for buttonPos, fct, text_button in zip(buttonsPosition, fcts, texts_button) :
            self.mainView.buttonList[buttonPos]["command"] = fct
            self.mainView.buttonList[buttonPos]["text"] = text_button

    def trainingMode(self, root):
        root.destroy()
        root = tk.Tk()
        TrainingController(self, root, self.operators, self.operator_number, self.plate_number)
        root.mainloop()

    def onlineMode(self, root):
        root.destroy()
        root = tk.Tk()
        ConnectionMaker(self, root, self.operators, self.operator_number, self.plate_number)
        root.mainloop()

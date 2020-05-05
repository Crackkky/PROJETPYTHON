import sys
import tkinter as tk

from tkinter import *

from Projet.Controller.trainingController import TrainingController
from Projet.Model.jisoo import playerMode
from Projet.Model.lisa import serverMode
from Projet.Model.training import trainingMode
from Projet.View.mainView import MainView


class MainController :
    def __init__(self):
        root = tk.Tk()
        self.mainView = MainView(root)
        buttonsPosition = [self.mainView.trainingButton, self.mainView.serverButton, self.mainView.clientButton, self.mainView.quitButton]
        fcts = [lambda : self.training(root), lambda :serverMode(), lambda :playerMode(), lambda :sys.exit()]
        for buttonPos, fct in zip(buttonsPosition, fcts) :
            self.mainView.buttonList[buttonPos]["command"] = fct
        root.mainloop()

    def training(self, root):
        root.destroy()
        TrainingController()

    def server(self, root):
        print("TODO")

    def client(self, root):
        print("TODO")


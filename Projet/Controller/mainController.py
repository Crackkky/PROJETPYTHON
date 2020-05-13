import tkinter as tk

from tkinter import *

from Projet.Controller.trainingController import TrainingController
from Projet.Model.jisoo import playerMode
from Projet.Model.lisa import serverMode
from Projet.View.mainView import MainView


class MainController:
    def __init__(self, root):
        self.mainView = MainView(root)
        self.mainView.label['text'] = '블랙핑크 하우스 환영합니!'
        texts_button = ["Play in Training", "Play as Lisa (Server)", "Play as Jisoo (Client)", "Quit"]
        buttonsPosition = [self.mainView.trainingButton, self.mainView.serverButton, self.mainView.clientButton,
                           self.mainView.quitButton]
        fcts = [lambda: self.training(root), lambda: serverMode(), lambda: playerMode(), lambda: sys.exit()]
        for buttonPos, fct, text_button in zip(buttonsPosition, fcts, texts_button):
            self.mainView.buttonList[buttonPos]["command"] = fct
            self.mainView.buttonList[buttonPos]["text"] = text_button

    def training(self, root):
        root.destroy()
        root = tk.Tk()
        TrainingController(self, root)
        root.mainloop()

    def server(self, root):
        print("TODO")

    def client(self, root):
        print("TODO")

import sys

from Projet.Model.jisoo import playerMode
from Projet.Model.lisa import serverMode
from Projet.Model.training import trainingMode
from Projet.View.mainInterface import MainInterface


class MainController :
    def __init__(self, root):
        self.mainView = MainInterface(root)
        buttonsPosition = [self.mainView.trainingButton, self.mainView.lisaButton, self.mainView.jisooButton, self.mainView.quitButton]
        fcts = [lambda :trainingMode(), lambda :serverMode(), lambda :playerMode(), lambda :sys.exit()]
        for buttonPos, fct in zip(buttonsPosition, fcts) :
            self.mainView.buttonList[buttonPos]["command"] = fct
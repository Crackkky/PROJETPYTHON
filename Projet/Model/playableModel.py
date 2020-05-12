import itertools

from Projet.Model.plateModel import PlateModel
from Projet.Model.util import *


class PlayableModel(PlateModel):
    def __init__(self):
        super(PlayableModel, self).__init__()
        self.history = []

    def doPlay(self, indice1, operator, indice2):
        operationFromArray(self.history, self.selectedPlates, indice1, operator, indice2)
        self.lenSelectedPlate = len(self.selectedPlates)

    def historyToString(self):
        res = ""
        for i in self.history:
            res += "\n" + i.operation.toString()
        return res
import itertools

from Projet.Model.tileModel import TileModel
from Projet.Model.util import *


class PlayableModel(TileModel):
    def __init__(self):
        super(PlayableModel, self).__init__()
        self.history = []

    def doPlay(self, indice1, operator, indice2):
        operationFromArray(self.history, self.selectedTiles, indice1, operator, indice2)
        self.lenSelectedTile = len(self.selectedTiles)

    def historyToString(self):
        res = ""
        for i in self.history:
            res += "\n" + i.operation.toString()
        return res
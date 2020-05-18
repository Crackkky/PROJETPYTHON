import itertools
from Projet.Model.util import *


class TileModel:
    def __init__(self):
        self.empty()

    def initGame(self):
        self.goal, self.originalTiles = generateGoalTiles(100, 999, 27)
        self.selectedTiles = self.originalTiles.copy()
        self.lenSelectedTile = len(self.selectedTiles)

    def empty(self):
        self.goal = None
        self.originalTiles = []
        self.selectedTiles = []
        self.lenSelectedTile = None

    def getDifference(self, value = -1):
        if self.lenSelectedTile == 1:
            return abs(self.goal - self.selectedTiles[0].getNumber())
        if value is not -1:
            return abs(self.goal-value)

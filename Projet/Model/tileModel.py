import itertools
from Projet.Model.util import *

DEBUG_VAR = True


class TileModel:
    def __init__(self):
        self.empty()

    def initGame(self):
        if DEBUG_VAR:
            self.goal = 170
            self.originalTiles = [Tile(10), Tile(10), Tile(25), Tile(25), Tile(50), Tile(50)]
        else:
            self.goal, self.originalTiles = generateGoalTiles(100, 999, 27)
        self.selectedTiles = self.originalTiles.copy()
        self.lenSelectedTile = len(self.selectedTiles)

    def empty(self):
        self.goal = None
        self.originalTiles = []
        self.selectedTiles = []
        self.lenSelectedTile = None

    def getDifference(self, value=-1):
        if self.lenSelectedTile == 1:
            return abs(self.goal - self.selectedTiles[0].getNumber())
        if value is not -1:
            return abs(self.goal - value)

import itertools
from Projet.Model.util import *


class PlateModel:
    def __init__(self):
        self.empty()

    def initGame(self):
        self.goal, self.originalPlates = generateGoalPlates(100, 999, 27)
        self.selectedPlates = self.originalPlates.copy()
        self.lenSelectedPlate = len(self.selectedPlates)

    def empty(self):
        self.goal = None
        self.originalPlates = []
        self.selectedPlates = []
        self.lenSelectedPlate = None

    def getDifference(self):
        if self.lenSelectedPlate == 1:
            return abs(self.goal - self.selectedPlates[0].getNumber())
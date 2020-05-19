import itertools

from Projet.Model.playableModel import PlayableModel
from Projet.Model.util import *


class TrainingModel(PlayableModel):
    def __init__(self):
        super(TrainingModel, self).__init__()
        self.selectedTiles = [Tile(0)]
        self.initGame()

    # Come back to the previous step in the history
    def previousHistory(self):
        previousStepIndex = len(self.history)
        if previousStepIndex > 0:
            self.selectedTiles = self.history[previousStepIndex - 1].tileArray
            self.history = self.removeHistory(self.history, previousStepIndex - 1)
            self.lenSelectedTile = len(self.selectedTiles)

    # Daisy bot will get the solution for you
    def findSolution(self):
        tileArray = self.originalTiles
        objective = self.goal
        operatorsStr = OPERATORS
        operators = operatorsStr
        operatorsCartesian = list(itertools.product(range(0, len(operators)), repeat=len(tileArray) - 1))
        tilePermutation = list(itertools.permutations(range(0, len(tileArray))))
        best = None
        # Pour chaque plaque
        for i in tilePermutation:
            # Pour chaque operateur
            for j in operatorsCartesian:
                stringOperation = ""
                for k in range(0, len(tileArray) - 1):
                    stringOperation += '('
                stringOperation += tileArray[i[0]].toString()
                # Nous generons l'operation en string
                for k in range(1, len(tileArray)):
                    stringOperation += operators[j[k - 1]] + tileArray[i[k]].toString() + ')'
                value = eval(stringOperation)
                actualDifference = abs(objective - value)
                if best is None or actualDifference < difference:
                    difference = actualDifference
                    best = stringOperation
                    if difference == 0:
                        break
        return best, int(difference)

    # Delete the history
    def removeHistory(self, array, index):
        del array[index:len(array)]
        return array

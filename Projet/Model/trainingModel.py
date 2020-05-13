import itertools

from Projet.Model.playableModel import PlayableModel
from Projet.Model.util import *


class TrainingModel(PlayableModel):
    def __init__(self):
        super(TrainingModel, self).__init__()
        self.initGame()

    def previousHistory(self):
        previousStepIndex = len(self.history)
        if previousStepIndex > 0:
            self.selectedPlates = self.history[previousStepIndex - 1].plateArray
            self.history = self.removeHistory(self.history, previousStepIndex - 1)
            self.lenSelectedPlate = len(self.selectedPlates)

    def findSolution(self):
        plateArray = self.originalPlates
        objective = self.goal
        operatorsStr = OPERATORS
        operators = operatorsStr
        operatorsCartesian = list(itertools.product(range(0, len(operators)), repeat=len(plateArray) - 1))
        platePermutation = list(itertools.permutations(range(0, len(plateArray))))
        best = None
        # Pour chaque plaque
        for i in platePermutation:
            # Pour chaque operateur
            for j in operatorsCartesian:
                stringOperation = ""
                for k in range(0, len(plateArray) - 1):
                    stringOperation += '('
                stringOperation += plateArray[i[0]].toString()
                # Nous generons l'operation en string
                for k in range(1, len(plateArray)):
                    stringOperation += operators[j[k - 1]] + plateArray[i[k]].toString() + ')'
                value = eval(stringOperation)
                actualDifference = abs(objective - value)
                if best is None or actualDifference < difference:
                    difference = actualDifference
                    best = stringOperation
                    if difference == 0:
                        break
        return best, int(difference)

    def removeHistory(self, array, index):
        del array[index:len(array)]
        return array

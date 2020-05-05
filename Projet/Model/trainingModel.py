import itertools
from random import *

from Projet.Model.util import *


class TrainingModel():
    def __init__(self):
        self.goal, self.originalPlates = generateGoalPlates(100, 999, 27)
        self.selectedPlates = self.originalPlates.copy()
        self.history = []
        self.lenSelectedPlate = len(self.selectedPlates)
        # yes = True
        #
        # while yes:
        #
        #     goal, originalPlates = self.generateGoalPlates(100, 999, 27)
        #     selectedPlates = originalPlates.copy()
        #
        #     # selectedPlates = [Plate(2), Plate(4), Plate(25), Plate(1), Plate(75), Plate(8)]
        #     history = []
        #     lenSelectedPlate = len(selectedPlates)
        #
        #     # Start training mode
        #     while lenSelectedPlate != 1:
        #         while True:
        #             #  Menu time!
        #             menuSelection = chooseMenu()
        #             if menuSelection == 1:  # TODO dur?
        #                 userSelections = chooseOperation(selectedPlates)
        #
        #                 # Do stuff with your plates
        #                 try:
        #                     operationFromArray(history, selectedPlates, userSelections[0], userSelections[1],userSelections[2])
        #                     lenSelectedPlate = len(selectedPlates)
        #                     break
        #                 except Exception as e:
        #                     print(e)
        #                     printArray(selectedPlates)
        #             elif menuSelection == 2:  # TODO Durdur
        #                 printArray(history)
        #             elif menuSelection == 3:  # TODO Durdur
        #                 previousStepIndex = choosePreviousStep(len(history))
        #                 selectedPlates = history[previousStepIndex].plateArray
        #                 history = self.removeHistory(history, previousStepIndex)
        #             elif menuSelection == 4:  # TODO Durdur
        #                 try:
        #                     best = self.findSolution(originalPlates, goal)
        #                     selectedPlates = [Plate(int(eval(best[0])))]
        #                     lenSelectedPlate = len(selectedPlates)
        #                     bestLisible = best[0].replace('(', '').replace(')', '')
        #                     break
        #                 except Exception as e:
        #                     print(e)
        #             elif menuSelection == 0:  # TODO Durdur
        #                 sys.exit()
        #
        #     yes = chooseYesNo()


    def removeHistory(array, index):
        del array[index:len(array)]
        return array


    def findSolution(plateArray, objective, operatorsStr):
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



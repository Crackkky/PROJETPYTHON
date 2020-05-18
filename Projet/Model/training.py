import itertools
import sys
from random import *

from Projet.Model.operation import *
from Projet.Model.tile import *
from Projet.Model.step import *
from Projet.Model.util import *


# FUNCTION DEF

def removeHistory(array, index):
    print('remove')
    printArray(array)
    print(index)
    del array[index:len(array)]
    printArray(array)
    return array


def findSolution(tileArray, objective):
    print("\nPlease wait, Daisy OBVIOUSLY heard your request...\nJust let her some time to think about it...")
    operators = '*+/-'
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


# FUNCTION DEF


def trainingMode():
    print('Welcome in the training mode !')
    yes = True

    while yes:

        goal, originalTiles = generateGoalTiles(100, 999, 27)
        selectedTiles = originalTiles.copy()

        # selectedTiles = [Tile(2), Tile(4), Tile(25), Tile(1), Tile(75), Tile(8)]
        history = []
        lenSelectedTile = len(selectedTiles)

        # Start training mode
        while lenSelectedTile != 1:
            while True:
                # Choose a tile
                print('You have : ')
                printArray(selectedTiles)
                print('You must find : ' + str(goal) + '\n')

                #  Menu time!
                menuSelection = chooseMenu()
                if menuSelection == 1:  # TODO dur?
                    userSelections = chooseOperation(selectedTiles)

                    # Do stuff with your tiles
                    try:
                        operationFromArray(history, selectedTiles, userSelections[0], userSelections[1],
                                           userSelections[2])
                        lenSelectedTile = len(selectedTiles)
                        break
                    except Exception as e:
                        print(e)
                        printArray(selectedTiles)
                    print('')
                elif menuSelection == 2:  # TODO Durdur
                    print('\nYou\'ve previously done : ')
                    printArray(history)
                    print('')
                elif menuSelection == 3:  # TODO Durdur
                    print('\nYou\'ve previously done : ')
                    printArray(history)
                    previousStepIndex = choosePreviousStep(len(history))
                    selectedTiles = history[previousStepIndex].tileArray
                    history = removeHistory(history, previousStepIndex)
                    printArray(selectedTiles)
                    print('')
                elif menuSelection == 4:  # TODO Durdur
                    try:
                        best = findSolution(originalTiles, goal)
                        selectedTiles = [Tile(int(eval(best[0])))]
                        lenSelectedTile = len(selectedTiles)
                        bestLisible = best[0].replace('(', '').replace(')', '')
                        print("Best solution :", bestLisible, " = ", selectedTiles[0].getNumber(), ', that\'s ',
                              best[1],
                              " different from the solution (operations executed from left to right).\nThanks Daisy <3")
                        break
                    except Exception as e:
                        print(e)
                elif menuSelection == 0:  # TODO Durdur
                    print('\nYou\'ve chosen to quit, bye-bye ! ')
                    sys.exit()
            print('______________________________________________________')
            print('')

        print('Your last tile is : ')
        printArray(selectedTiles)
        print('The goal was : ')
        print(goal)

        print('Play again?')
        yes = chooseYesNo()

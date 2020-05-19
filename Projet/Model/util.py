import time
from random import randint

from Projet.Model.IvyModel import *
from Projet.Model.operation import Operation
from Projet.Model.tile import Tile
from Projet.Model.step import Step

stop = False
TILE_NUMBER = 6
DEFAULT_TIME = 45
MIN_GOAL = 100
MAX_GOAL = 999
OPERATORS = '*+/-'
OPERATOR_NUMBER = len(OPERATORS)
POSSIBLE_TILES = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
SCORE = 0
OPPONENT_SCORE = 0


# Generate the usable tiles and goal
def generateGoalTiles(goalMin, goalMax, nbTile):
    goal = randint(goalMin, goalMax)
    possibleTiles = POSSIBLE_TILES.copy()
    selectedTiles = []

    # Generate tiles
    for i in range(1, 7):
        tileNumber = randint(0, nbTile)
        selectedTiles.append(Tile(possibleTiles[tileNumber]))
        possibleTiles.pop(tileNumber)
        nbTile -= 1

    return goal, selectedTiles


# Return the message or "" else
def parseMessages(msg, regex):
    import re
    res = ""

    regex_search = re.search(regex, msg)
    if regex_search:
        res = regex_search.group(1)

    return res


# Do the operation from the array between index1 and index2
# Append the result and remove the used tiles
def operationFromArray(history, tileArray, index1, operator, index2):
    try:
        operation = Operation(tileArray[index1].getNumber(), operator, tileArray[index2].getNumber())
        history.append(Step(operation, tileArray))
        tileArray.append(Tile(operation.do()))

    except Exception as e:
        raise e

    if index1 < index2:
        tileArray.remove(tileArray[index2])
        tileArray.remove(tileArray[index1])
    else:
        tileArray.remove(tileArray[index1])
        tileArray.remove(tileArray[index2])


# Parse a message if there is one, else return ""
def getMessage(ivyObject, regex):
    message = ""
    if ivyObject.messages:
        message = ivyObject.messages.pop()[0]
        # print('MESSAGE : ', message)
    return parseMessages(message, regex)

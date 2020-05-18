import threading
import time
from random import randint

from Projet.Model.IvyProject import *
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


def chooseMenu():
    while True:
        print('Choose an option:')
        print('0. Quit')
        print('1. Do an operation')
        print('2. See operation history')
        print('3. Return to a previous step')
        print('4. Get the solution from the wonderful DaisyBot!')
        index = int(input('(Enter the number) => '))
        if index > 4 or index < 0:  # TODO 4 en durud
            print('Erreur Menu !')
        else:
            return index


def chooseOperator():
    while True:
        operator = input('Choose an operator in [+ \\ - \\ * \\ /] : ')
        if operator != '+' and operator != '-' and operator != '*' and operator != '/':  # TODO Dur dur
            print('Erreur operator !')
        else:
            print('You\'ve chosen : ' + operator)
            return operator


def chooseYesNo():
    while True:
        yesNo = input('Please enter "Y" or "N" : ')
        if yesNo == 'Y':  # TODO DUR
            return True
        elif yesNo == 'N':  # TODO DUR
            return False
        else:
            print('Erreur operator !')


def chooseOperation(selectedTiles):
    lenSelectedTile = len(selectedTiles)
    print('')
    printArray(selectedTiles)
    userSelection1 = chooseIndex(selectedTiles, lenSelectedTile)

    print('')
    userSelectionOp = chooseOperator()

    print('')
    printArray(selectedTiles)
    userSelection2 = chooseIndex(selectedTiles, lenSelectedTile)
    while userSelection1 == userSelection2:
        print('Please don\'t choose the same tile twice!')
        userSelection2 = chooseIndex(selectedTiles, lenSelectedTile)

    return [userSelection1, userSelectionOp, userSelection2]


def chooseIndex(selectedTiles, lenArray):
    while True:
        while True:
            try:
                index = int(input('Choose a tile number : '))
                break
            except Exception as e:
                print(e)
        if index > lenArray or index <= 0:
            print('Erreur index !')
        else:
            print('You\'ve chosen : ' + str(selectedTiles[index - 1].getNumber()))
            return index - 1


def choosePreviousStep(lenArray):
    while True:
        index = int(input('Choose a step to come back to : '))
        if index > lenArray or index <= 0:
            print('Erreur index !')
        else:
            print('Let\'s get back in time !')
            return index - 1


def closestNumber(num1, num2, goal):
    if abs(num1 - goal) == abs(num2 - goal):
        return -1
    elif abs(num1 - goal) < abs(num2 - goal):
        return num1
    else:
        return num2


# Create Ivy object and initialise a connexion
def connexionIvy(opponentName):
    ivyObject = IvyModel('127.0.0.1:2010')
    ivyObject.bindIvy('(' + opponentName + ' says: .*)')
    time.sleep(0.1)
    return ivyObject


# Start an online game
def gameStart(ivyObject, goal, selectedTiles, playerName, opponentName, gameTime):
    global stop
    print('')
    print('The game will now start !')
    print('')

    timeEnd = time.time() + gameTime if gameTime != 0 else DEFAULT_TIME

    stopFromOther = False
    stop = False

    while time.time() < timeEnd and not stop:
        if getMessage(ivyObject, opponentName + ' says: stop(.*)'):
            stop = True
            stopFromOther = True
        time.sleep(0.1)

    if not stop and not stopFromOther:
        return False
    elif stop and not stopFromOther:
        sendMessage(playerName + ' says: stop!')

    if stopFromOther:
        print('Your opponent found before you!')
        print('Wait till the other player finish!')
        answer = int(waitMessage(ivyObject, opponentName + ' says: answer = (.*)'))
        if answer == 0:
            print('Your opponent FAILED!')
            scorePlusPlus(True)
        else:
            print('Your opponent WON!')
            scorePlusPlus(False)
    else:
        answer = suggestSolution([], goal, selectedTiles)
        if answer == goal:
            sendMessage(playerName + ' says: answer = ' + str(answer))
            scorePlusPlus(True)
        else:
            sendMessage(playerName + ' says: answer = 0')
            scorePlusPlus(False)

    return True


def getNumberOfPlayer():
    listPlayer = IvyGetApplicationList()
    return len(listPlayer)


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
    # print('MSG :', msg)
    # print('RGX :', regex)
    if regex_search:
        res = regex_search.group(1)
        # print('PARSED : \"' + res + '\"')

    return res


# Do the operation from the array between index1 and index2
# Append the result and remove the used tiles
def operationFromArray(history, tileArray, index1, operator, index2):
    # print('Vous essayez de faire : ' + str(tileArray[index1].getNumber()) + operator
    # + str(tileArray[index2].getNumber()))

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


def printArray(array):
    tabString = []
    if len(array) > 0:
        for i in range(0, len(array)):
            tabString.append(array[i].toString())
        print(tabString)
    else:
        print('Empty array!')


def receivePlayAgain(name, ivyObject):
    while True:
        playAgain = getMessage(ivyObject, name + ' says: again (.*)')
        if playAgain == 'not':
            return False
        elif playAgain == '!':
            return True
        time.sleep(0.1)


def replayPlayer(name, nameOpponent, ivyObject):
    print('Play again?')
    if chooseYesNo():
        sendMessage(name + ' says: again !')
        print('Waiting for the other player\'s reply...')
        if receivePlayAgain(nameOpponent, ivyObject):
            print('OK let\'s play again')
            return True
        else:
            print('The player don\'t want to play again')
            return False
    else:
        sendMessage(name + ' says: again not')
        return False


def replayServer(name, nameOpponent, ivyObject):
    print('Waiting if the other play want to play again...')
    if receivePlayAgain(nameOpponent, ivyObject):
        print('Play again?')
        if chooseYesNo():
            sendMessage(name + ' says: again !')
            print('OK let\'s play again')
            return True
        else:
            sendMessage(name + ' says: again not')
            return False
    else:
        print('The player don\'t want to play again')
        return False


def scorePlusPlus(player):
    global SCORE, OPPONENT_SCORE
    if player:
        SCORE += 1
    else:
        OPPONENT_SCORE += 1


def scoreToString(player):
    global SCORE, OPPONENT_SCORE
    if player:
        return str(SCORE)
    else:
        return str(OPPONENT_SCORE)


# Suggest a solution
def suggestSolution(history, goal, selectedTiles):
    lenSelectedTile = len(selectedTiles)
    while lenSelectedTile != 1:
        while True:
            # Choose a tile
            print('You have : ')
            printArray(selectedTiles)
            print('You must find : ' + str(goal) + '\n')
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

        print('______________________________________________________')
        print('')

    print('Your last tile is : ')
    printArray(selectedTiles)
    print('The goal was : ')
    print(goal)

    return selectedTiles[0].getNumber()


# Ask in another thread for an input
def thread_function():
    global stop
    input('')
    stop = True


# Parse a message if there is one, else return ""
def getMessage(ivyObject, regex):
    message = ""
    if ivyObject.messages:
        message = ivyObject.messages.pop()[0]
        # print('MESSAGE : ', message)
    return parseMessages(message, regex)


def waitMessage(ivyObject, regex):
    while True:
        message = getMessage(ivyObject, regex)
        if message:
            return message
        time.sleep(0.1)

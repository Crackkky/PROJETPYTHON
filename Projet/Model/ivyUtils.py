# Create Ivy object and initialise a connexion
import time

from Projet.Model.IvyProject import IvyModel, sendMessage, IvyGetApplicationList
from Projet.Model.util import suggestSolution, chooseYesNo

stop = False
PLATE_NUMBER = 6
DEFAULT_TIME = 45
OPERATORS = '*+/-'
OPERATOR_NUMBER = len(OPERATORS)
POSSIBLE_PLATES = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
SCORE = 0
OPPONENT_SCORE = 0


def closestNumber(num1, num2, goal):
    if abs(num1 - goal) == abs(num2 - goal):
        return -1
    elif abs(num1 - goal) < abs(num2 - goal):
        return num1
    else:
        return num2


# Create Ivy object and initialise a connexion
def connexionIvy(opponentName):
    ivyObject = IvyModel('127.0.0.1:2487')
    ivyObject.bindIvy('(' + opponentName + ' says: .*)')
    time.sleep(0.1)
    return ivyObject


# Start an online game
def gameStart(ivyObject, goal, selectedPlates, playerName, opponentName, gameTime):
    global stop

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
        answer = int(waitMessage(ivyObject, opponentName + ' says: answer = (.*)'))
        if answer == 0:
            scorePlusPlus(True)
        else:
            scorePlusPlus(False)
    else:
        answer = suggestSolution([], goal, selectedPlates)
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


# Return the message or "" else
def parseMessages(msg, regex):
    import re
    res = ""

    regex_search = re.search(regex, msg)
    if regex_search:
        res = regex_search.group(1)

    return res


def receivePlayAgain(name, ivyObject):
    while True:
        playAgain = getMessage(ivyObject, name + ' says: again (.*)')
        if playAgain == 'not':
            return False
        elif playAgain == '!':
            return True
        time.sleep(0.1)


def replayPlayer(name, nameOpponent, ivyObject):
    if chooseYesNo():
        sendMessage(name + ' says: again !')
        if receivePlayAgain(nameOpponent, ivyObject):
            return True
        else:
            return False
    else:
        sendMessage(name + ' says: again not')
        return False


def replayServer(name, nameOpponent, ivyObject):
    if receivePlayAgain(nameOpponent, ivyObject):
        if chooseYesNo():
            sendMessage(name + ' says: again !')
            return True
        else:
            sendMessage(name + ' says: again not')
            return False
    else:
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
    return parseMessages(message, regex)


def waitMessage(ivyObject, regex):
    while True:
        message = getMessage(ivyObject, regex)
        if message:
            return message
        time.sleep(0.1)

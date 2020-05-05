import threading
import time
from random import randint

from Projet.Model.IvyProject import *
from Projet.Model.operation import Operation
from Projet.Model.plate import Plate
from Projet.Model.step import Step

stop = False
PLATE_NUMBER = 6
OPERATORS ='*+/-'
OPERATOR_NUMBER = len(OPERATORS)
POSSIBLE_PLATES = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]


def generateGoalPlates(goalMin, goalMax, nbPlate):
    goal = randint(goalMin, goalMax)
    possiblePlates = POSSIBLE_PLATES
    # TODO durian
    selectedPlates = []

    # Generate plates
    for i in range(0, PLATE_NUMBER):
        plateNumber = randint(0, nbPlate)  # TODO 27 durrrrrrrrrr
        selectedPlates.append(Plate(possiblePlates[plateNumber]))

    return goal, selectedPlates

def chooseMenu():
    while True:
        print('Choose an option:')
        print('0. Quit')
        print('1. Do an operation')
        print('2. See operation history')
        print('3. Return to a previous step')
        print('4. Get the solution from the wonderful DaisyBot!')
        index = int(input('(Enter the number) => '))
        if index > 4 or index < 0:  # TODO 2 en durud
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


def chooseOperation(selectedPlates):
    lenSelectedPlate = len(selectedPlates)
    print('')
    printArray(selectedPlates)
    userSelection1 = chooseIndex(selectedPlates, lenSelectedPlate)

    print('')
    userSelectionOp = chooseOperator()

    print('')
    printArray(selectedPlates)
    userSelection2 = chooseIndex(selectedPlates, lenSelectedPlate)
    while userSelection1 == userSelection2:
        print('Please don\'t choose the same plate twice!')
        userSelection2 = chooseIndex(selectedPlates, lenSelectedPlate)

    return [userSelection1, userSelectionOp, userSelection2]


def chooseIndex(selectedPlates, lenArray):
    while True:
        while True:
            try:
                index = int(input('Choose a plate number : '))
                break
            except Exception as e:
                print(e)
        if index > lenArray or index <= 0:
            print('Erreur index !')
        else:
            print('You\'ve chosen : ' + str(selectedPlates[index - 1].getNumber()))
            return index - 1


def choosePreviousStep(lenArray):
    while True:
        index = int(input('Choose a step to come back to : '))
        if index > lenArray or index <= 0:
            print('Erreur index !')
        else:
            print('Let\'s get back in time !')
            return index - 1


def connexionIvy(opponentName):
    ivyObject = IvyModel('127.0.0.1:2010')
    ivyObject.bindIvyServer('(' + opponentName + ' says: .*)')
    time.sleep(1)
    return ivyObject


def gameStart(ivyProject, goal, selectedPlates, playerName, opponentName):
    global stop
    print('')
    print('The game will now start !')
    print('')

    timeEnd = time.time() + 45

    x = threading.Thread(target=thread_function)
    x.start()

    stopFromOther = False

    while time.time() < timeEnd and not stop:
        message = ""
        # Wait for a signal from the server or the user
        if ivyProject.messages:
            message = ivyProject.messages.pop()[0]
            if parseMessages(message, opponentName + ' says: stop(.*)'):
                # print('MESSAGE :', message)
                stop = True
                stopFromOther = True
        time.sleep(0.1)
        # print('1')

    if not stopFromOther:
        sendMessage(playerName + ' says: ', 'stop!')
    else:
        print('Too late! Enter anything to continue : ')

    x.join()

    print('OK')
    if stopFromOther:
        print('Wait till the other player finish !')
        while True:
            message = ""
            if ivyProject.messages:
                message = ivyProject.messages.pop()[0]
            answer = parseMessages(message, opponentName+' says: answer = (.*)')
            if answer:
                print('ANSWER :', answer)
    else:
        history = []
        answer = suggestSolution(history, goal, selectedPlates)
        print('ANSWER :', answer)
        print('SENT :', playerName+' says: answer = ' + str(answer))
        sendMessage(playerName+' says: ', 'answer = ' + str(answer))


def parseMessages(msg, regex):
    import re
    res = ""

    regex_search = re.search(regex, msg)
    if regex_search:
        res = regex_search.group(1)
        # print('PARSED : \"' + res + '\"')

    return res




def operationFromArray(history, plateArray, index1, operator, index2):
    # print('Vous essayez de faire : ' + str(plateArray[index1].getNumber()) + operator
    # + str(plateArray[index2].getNumber()))

    try:
        operation = Operation(plateArray[index1].getNumber(), operator, plateArray[index2].getNumber())
        history.append(Step(operation, plateArray))
        plateArray.append(Plate(operation.do()))

    except Exception as e:
        raise e

    if index1 < index2:
        plateArray.remove(plateArray[index2])
        plateArray.remove(plateArray[index1])
    else:
        plateArray.remove(plateArray[index1])
        plateArray.remove(plateArray[index2])


def printArray(array):
    tabString = []
    if len(array) > 0:
        for i in range(0, len(array)):
            tabString.append(array[i].toString())
        print(tabString)
    else:
        print('Empty array!')


def suggestSolution(history, goal, selectedPlates):
    lenSelectedPlate = len(selectedPlates)
    while lenSelectedPlate != 1:
        while True:
            # Choose a plate
            print('You have : ')
            printArray(selectedPlates)
            print('You must find : ' + str(goal) + '\n')
            userSelections = chooseOperation(selectedPlates)

            # Do stuff with your plates
            try:
                operationFromArray(history, selectedPlates, userSelections[0], userSelections[1],
                                   userSelections[2])
                lenSelectedPlate = len(selectedPlates)
                break
            except Exception as e:
                print(e)
                printArray(selectedPlates)
            print('')

        print('______________________________________________________')
        print('')

    print('Your last plate is : ')
    printArray(selectedPlates)
    print('The goal was : ')
    print(goal)

    return selectedPlates[0].getNumber()


def thread_function():
    global stop
    input('Stop? ==> ')
    stop = True

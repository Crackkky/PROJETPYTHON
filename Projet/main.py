import sys
from random import *
from Projet.plate import *
from Projet.operation import *
from Projet.step import *
import itertools


# FUNCTION DEF


def removeHistory(array, index):
    print('remove')
    printArray(array)
    print(index)
    del array[index:len(array)]
    printArray(array)
    return array


def operationFromArray(history, plateArray, index1, operator, index2):
    # print('Vous essayez de faire : ' + str(plateArray[index1].getNumber()) + operator
    # + str(plateArray[index2].getNumber()))

    try:
        print(index1)
        print(index2)
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


def chooseIndex(lenArray):
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


def chooseOperation(selectedPlates):
    lenSelectedPlate = len(selectedPlates)
    print('')
    printArray(selectedPlates)
    userSelection1 = chooseIndex(lenSelectedPlate)

    print('')
    userSelectionOp = chooseOperator()

    print('')
    printArray(selectedPlates)
    userSelection2 = chooseIndex(lenSelectedPlate)
    while userSelection1 == userSelection2:
        print('Please choose the same plate twice!')
        userSelection2 = chooseIndex(lenSelectedPlate)

    return [userSelection1, userSelectionOp, userSelection2]


def findSolution(history, plateArray, objective):
    print("\nPatientez, Daisy a FORCEMENT entendu votre demande...\nLaissez lui le temps d'y réfléchir...")
    operators = '*+/-'
    operatorsCartesian = list(itertools.product(range(0, len(operators)), repeat=len(plateArray)-1))
    platePermutation = list(itertools.permutations(range(0,len(plateArray))))
    best = None
    #Pour chaque plaque
    for i in platePermutation :
        #Pour chaque operateur
        for j in operatorsCartesian :
            stringOperation = ""
            for k in range(0, len(plateArray)-1) :
                stringOperation +='('
            stringOperation += plateArray[i[0]].toString()
            #Nous generons l'operation en string
            for k in range(1, len(plateArray)) :
                stringOperation += operators[j[k-1]] + plateArray[i[k]].toString() + ')'
            value = eval(stringOperation)
            actualDifference = abs(objective-value)
            if best == None or actualDifference < difference :
                difference = actualDifference
                best = stringOperation
                if difference == 0 :
                    break
    bestLisible = best.replace('(', '').replace(')','')
    print("La meilleur :", bestLisible, " avec ", eval(best),', donc ', difference," de différence de gauche à droite sans prendre en compte les priorités.\nMerci Daisy <3" )
    return best





# FUNCTION DEF


print('Welcome in the training mode !')

goal = randint(100, 999)
possiblePlates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
# TODO durian
selectedPlates = []

# Generate plates
for i in range(1, 7):
    plateNumber = randint(0, 27)  # TODO 27 durrrrrrrrrr
    selectedPlates.append(Plate(possiblePlates[plateNumber]))

selectedPlates = [Plate(2), Plate(4), Plate(25), Plate(1), Plate(75), Plate(8)]
history = []
lenSelectedPlate = len(selectedPlates)

# Start training mode
while lenSelectedPlate != 1:
    print("LENNNNNNNNNNNNNN")
    print(lenSelectedPlate)
    while True:
        # Choose a plate
        print('________________________')
        print('You have : ')
        printArray(selectedPlates)
        print('You must find : ' + str(goal) + '\n')

        #  Menu time!
        menuSelection = chooseMenu()
        if menuSelection == 1:  # TODO dur?
            userSelections = chooseOperation(selectedPlates)

            # Do stuff with your plates
            try:
                operationFromArray(history, selectedPlates, userSelections[0], userSelections[1], userSelections[2])
                lenSelectedPlate = len(selectedPlates)
                break
            except Exception as e:
                print(e)
                printArray(selectedPlates)
            print('')
        elif menuSelection == 2:  # TODO Durdur
            print('\nYou\'ve previously done : ')
            printArray(history)
            print('')
        elif menuSelection == 3:  # TODO Durdur
            print('\nYou\'ve previously done : ')
            printArray(history)
            previousStepIndex = choosePreviousStep(len(history))
            selectedPlates = history[previousStepIndex].plateArray
            history = removeHistory(history, previousStepIndex)
            printArray(selectedPlates)
            print('')
        elif menuSelection == 4:  # TODO Durdur
            try:
                findSolution(history, selectedPlates, goal)
                lenSelectedPlate = len(selectedPlates)
                print('Daisy found : ')
                printArray(selectedPlates)
                printArray(history)
                break
            except Exception as e:
                print(e)
        elif menuSelection == 0:  # TODO Durdur
            print('\nYou\'ve chosen to quit, bye-bye ! ')
            sys.exit()
    print('//////////////////////////')
    print('')

print('Your last plate is : ')
printArray(selectedPlates)
print('The goal was : ')
print(goal)

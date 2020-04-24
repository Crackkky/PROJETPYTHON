from random import *
from Projet.plate import *


# FUNCTION DEF


def chooseIndex():
    while True:
        index = int(input('Choose a plate number : '))
        if index > 6 or index <= 0:
            print('Erreur index ! \n')
        else:
            print('You\'ve chosen : ' + str(selectedPlates[index - 1].getNumber()))
            return index - 1


def chooseOperator():
    while True:
        operator = input('Choose an operator in [+ \\ - \\ * \\ /] : ')
        if operator != '+' and operator != '-' and operator != '*' and operator != '/':  # TODO Dur dur
            print('Erreur operator ! \n')
        else:
            print('You\'ve chosen : ' + operator)
            return operator


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

while True:
    # Choose a plate
    printPlateArray(selectedPlates)

    userSelection1 = chooseIndex()
    userSelectionOp = chooseOperator()
    userSelection2 = chooseIndex()

    # Add 2 plates
    try:
        operationArray(selectedPlates, userSelection1, userSelection2, userSelectionOp)
        break
    except Exception as e:
        print(e)
    print('')

print('')
printPlateArray(selectedPlates)

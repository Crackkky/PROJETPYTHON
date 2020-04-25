from Projet.operation import *


def printPlateArray(array):
    tabString = []
    for i in range(0, len(array)):
        tabString.append(array[i].getNumber())
    print(tabString)


def operationFromArray(history, plateArray, index1, operator, index2):
    # print('Vous essayez de faire : ' + str(plateArray[index1].getNumber()) + operator
    # + str(plateArray[index2].getNumber()))

    try:
        plateArray.append(plateArray[index1].operation(history, plateArray[index2], operator))
    except Exception as e:
        raise e

    if index1 < index2:
        plateArray.remove(plateArray[index2])
        plateArray.remove(plateArray[index1])
    else:
        plateArray.remove(plateArray[index1])
        plateArray.remove(plateArray[index2])


class Plate:
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    # Do : "first plate <operator> second plate."
    def operation(self, history, plate2, operator):
        try:
            operation = Operation(self.getNumber(), operator, plate2.getNumber())
        except Exception as e:
            raise e
        history.append(operation)
        # operation.printOperation()
        return Plate(operation.do())

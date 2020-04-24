def printPlateArray(array):
    tabString = []
    for i in range(0, len(array)):
        tabString.append(array[i].getNumber())
    print(tabString)


def operationArray(plateArray, index1, index2, operator):
    # print('Vous essayez de faire : ' + str(plateArray[index1].getNumber()) + operator
    # + str(plateArray[index2].getNumber()))
    try:
        plateArray.append(plateArray[index1].operation(plateArray[index2], operator))
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
    def operation(self, plate2, operator):
        if operator == '/' and (self.getNumber() % plate2.getNumber() != 0):
            # print('Reste = ' + str(plate2.getNumber() % self.getNumber()))
            raise Exception('Erreur le reste de le division n\'est pas nul!')

        if operator == '-' and (self.getNumber() - plate2.getNumber() < 0):
            print('<0 !!!!!!')
            print(plate2.getNumber() - self.getNumber())
            return Plate(plate2.getNumber() - self.getNumber())
        else:
            print(int(eval(str(self.getNumber()) + operator + str(plate2.getNumber()))))
            return Plate(int(eval(str(self.getNumber()) + operator + str(plate2.getNumber()))))

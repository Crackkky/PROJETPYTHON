


def printPlateArray(array):
    tabString = []
    for i in range(0, len(array)):
        tabString.append(array[i].getNumber())
    print(tabString)

class plate():
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def operation(self, plateArray, index): #TODO add parameter to choose operation, evaluate?
        plateArray.append(self.add(plateArray[index]))
        plateArray.remove(plateArray[index])
        plateArray.remove(self)

    def add(self, plate2):
        return plate(self.getNumber() + plate2.getNumber())













































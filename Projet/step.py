def plateArrayToString(array):
    tabString = []
    for i in range(0, len(array)):
        tabString.append(array[i].toString())
    return str(tabString)

# One step AFTER an operation
class Step:
    def __init__(self, operation, plateArray):
        self.operation = operation
        self.plateArray = plateArray.copy()

    def toString(self):
        return self.operation.toString() + ', Plate Array : ' + plateArrayToString(self.plateArray) # + ' \n'

    def getOperation(self):
        return self.operation

    def setOperation(self, operation):
        if operation is not None:
            self.operation = operation

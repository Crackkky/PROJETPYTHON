def arrayToString(array):
    stringRes = '['
    if len(array) > 0:
        for i in range(0, len(array)):
            if i != len(array)-1:
                stringRes += array[i].toString() + ', '
            else:
                stringRes += array[i].toString()
        return stringRes + ']'
    else:
        return 'None'


# One step AFTER an operation
class Step:
    def __init__(self, operation, tileArray):
        self.operation = operation
        self.tileArray = tileArray.copy()

    def toString(self):
        return self.operation.toString() + ', Tile Array : ' + arrayToString(self.tileArray)

    def getOperation(self):
        return self.operation

    def getTileArray(self):
        return self.tileArray

    def setOperation(self, operation):
        if operation is not None:
            self.operation = operation

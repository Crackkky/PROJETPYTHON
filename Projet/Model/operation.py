class Operation:
    def __init__(self, G, op, D):
        if op == '-' and (G - D < 0):
            self.D = G
            self.G = D
        elif op == '/' and (G % D != 0):
            # print('Reste = ' + str(plate2.getNumber() % self.getNumber()))
            raise Exception('Erreur le reste de le division n\'est pas nul!')
        else:
            self.G = G
            self.D = D
        self.op = op

    def getG(self):
        return self.G

    def getOp(self):
        return self.op

    def getD(self):
        return self.D

    def toString(self):
        return str(str(self.getG()) + self.getOp() + str(self.getD()))

    # Do : "first plate <operator> second plate."
    def do(self):
        # print(int(eval(str(self.getG()) + str(self.getOp()) + str(self.getD()))))
        return int(eval(str(self.getG()) + self.getOp() + str(self.getD())))

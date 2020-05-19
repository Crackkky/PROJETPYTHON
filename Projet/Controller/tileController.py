import tkinter as tk


class TileController:
    def __init__(self, parent, model, view, OPERATORS):

        self.operators = OPERATORS
        self.operatorNumber = len(OPERATORS)
        self.firstTile = None
        self.secondTile = None
        self.operator = None

        self.model = model
        self.view = view

        self.parent = parent

    def updateView(self):

        self.firstTile = None
        self.secondTile = None
        self.operator = None

        self.view.goalLabel["text"] = "Goal\n" + str(self.model.goal)

        # completion des checKButtons des plaques
        for i in range(0, self.model.lenSelectedTile):
            checkButton = self.view.checkTileList[i]
            # x=i car si i utilisé directement, il est mis en attente jusqu'à l'appel, et i fini = au dernier
            self.completeButton(self.model.selectedTiles[i].toString(),
                                lambda x=i: self.checkMaxOfTile(x),
                                checkButton)
            checkButton["offvalue"] = -1
            checkButton.deselect()
            checkButton["onvalue"] = i

        # completion des checKButtons des plaques
        for i in range(0, len(self.view.checkOperatorList)):
            checkButton = self.view.checkOperatorList[i]
            # x=i car si i utilisé directement, il est mis en attente jusqu'à l'appel, et i fini = au dernier
            self.completeButton(self.operators[i], lambda x=i: self.checkMaxOfOperator(x), checkButton)
            checkButton["offvalue"] = -1
            checkButton.deselect()
            checkButton["onvalue"] = i



    # Controle qu'il n'y a que 2 plaques selectionnées, sinon retire la plus anciennce
    def checkMaxOfTile(self, pos):
        if self.firstTile == pos:
            self.firstTile = None
        elif self.secondTile == pos:
            self.secondTile = None
        elif self.firstTile is None:
            self.firstTile = pos
        elif self.secondTile is None:
            self.secondTile = pos
        else:
            self.view.checkTileList[self.secondTile].deselect()
            self.secondTile = self.firstTile
            self.firstTile = pos

    # Controle qu'il n'y a qu'une plaque de selectionnée, sinon la remplace
    def checkMaxOfOperator(self, pos):
        if self.operator == pos:
            self.operator = None
        elif self.operator is None:
            self.operator = pos
        else:
            self.view.checkOperatorList[self.operator].deselect()
            self.operator = pos

    def completeButton(self, text, fct, button):
        button["text"] = text
        button["command"] = fct

    def backMenu(self, root):
        root.after(100, lambda :root.destroy())
        new = tk.Tk()
        self.parent.__init__(new, self.operators, self.operatorNumber, self.maxTileNumber)
        new.mainloop()


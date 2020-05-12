import tkinter as tk

from Projet.Model.trainingModel import TrainingModel
from Projet.Model.util import PLATE_NUMBER, OPERATORS, OPERATOR_NUMBER
from Projet.View.trainingView import TrainingView


class PlateController:
    def __init__(self, parent, model, view):

        self.firstPlate = None
        self.secondPlate = None
        self.operator = None

        self.model = model
        self.view = view

        self.parent = parent

        self.updateView()

    def updateView(self):

        self.firstPlate = None
        self.secondPlate = None
        self.operator = None

        # completion des checKButtons des plaques
        for i in range(0, self.model.lenSelectedPlate):
            checkButton = self.view.checkPlateList[i]
            # x=i car si i utilisé directement, il est mis en attente jusqu'à l'appel, et i fini = au dernier
            self.completeButton(self.model.selectedPlates[i].toString(),
                                lambda x=i: self.checkMaxOfPlate(x),
                                checkButton)
            checkButton["offvalue"] = -1
            checkButton.deselect()
            checkButton["onvalue"] = i

        # completion des checKButtons des plaques
        for i in range(0, self.operatorNumber):
            checkButton = self.view.checkOperatorList[i]
            # x=i car si i utilisé directement, il est mis en attente jusqu'à l'appel, et i fini = au dernier
            self.completeButton(self.operators[i], lambda x=i: self.checkMaxOfOperator(x), checkButton)
            checkButton["offvalue"] = -1
            checkButton.deselect()
            checkButton["onvalue"] = i



    # Controle qu'il n'y a que 2 plaques selectionnées, sinon retire la plus anciennce
    def checkMaxOfPlate(self, pos):
        if self.firstPlate == pos:
            self.firstPlate = None
        elif self.secondPlate == pos:
            self.secondPlate = None
        elif self.firstPlate is None:
            self.firstPlate = pos
        elif self.secondPlate is None:
            self.secondPlate = pos
        else:
            self.view.checkPlateList[self.secondPlate].deselect()
            self.secondPlate = self.firstPlate
            self.firstPlate = pos

    # Controle qu'il n'y a qu'une plaque de selectionnée, sinon la remplace
    def checkMaxOfOperator(self, pos):
        if self.operator == pos:
            self.operator = None
        elif self.operator is None:
            self.operator = pos
        else:
            self.view.checkOperatorList[self.operator].deselect()
            self.operator = pos



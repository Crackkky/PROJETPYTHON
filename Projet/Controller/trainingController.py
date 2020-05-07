import tkinter as tk

from Projet.Model.trainingModel import TrainingModel
from Projet.Model.util import PLATE_NUMBER, OPERATORS, OPERATOR_NUMBER, operationFromArray
from Projet.View.trainingView import TrainingView


class TrainingController :
    def __init__(self, parent):
        root = tk.Tk()
        self.parent = parent
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.trainingModel = TrainingModel()
        self.trainingView = TrainingView(self.maxPlateNumber, OPERATOR_NUMBER, root)

        self.trainingView.validateButton["text"] = "Validate"
        self.trainingView.validateButton["command"] = lambda : self.validate()

        self.trainingView.backButton["text"] = "Back Step"
        self.trainingView.backButton["command"] = lambda : self.backStep()

        self.trainingView.returnButton["text"] = "Back"
        self.trainingView.returnButton["command"] = lambda : self.backMenu(root)

        self.trainingView.newButton["text"] = "New One"
        self.trainingView.newButton["command"] = lambda : self.newOne()

        self.trainingView.solutionButton["text"] = "Solution ?"

        self.update()
        root.mainloop()

    def validate(self) :
        if(self.firstPlate != None and self.secondPlate !=None and self.operator!=None) :
            self.trainingModel.doPlay(self.firstPlate,self.operators[self.operator],self.secondPlate)
            #Suppresion de l'affichage de la dernière plaque
            self.trainingView.checkPlateList[self.trainingModel.lenSelectedPlate].pack_forget()
            if (self.trainingModel.lenSelectedPlate == 1):
                self.trainingView.displayInfo("You got a difference of "
                                              + str(self.trainingModel.getDifference())
                                              + ", not Badr")
            else:
                self.trainingView.displayInfo()
            self.update()
        else :
            self.trainingView.displayInfo("Please, select 2 plates and 1 operator")

    def newOne(self):
        for i in range(self.maxPlateNumber) :
            self.trainingView.checkPlateList[i].pack(side='left')
        self.trainingModel = TrainingModel()
        self.update()

    def backStep(self):
        if (len(self.trainingModel.history) > 0):
            self.trainingView.checkPlateList[self.trainingModel.lenSelectedPlate].pack(side='left')
            self.trainingModel.previousHistory()
            self.update()
            self.trainingView.displayInfo()
        else :
            self.trainingView.displayInfo("History empty, please play before")

    def backMenu(self, root):
        root.destroy()
        self.parent.__init__()

    def update(self):
        self.firstPlate = None  # Position de la 1ère plaque
        self.secondPlate = None  # Position de la 2ème plaque
        self.operator = None  # position de l'operator
        self.trainingView.goalLabel["text"] = "Goal\n" + str(self.trainingModel.goal)
        self.trainingView.historyLabel["text"] = "History" + self.trainingModel.historyToString()

        # completion des checKButtons des plaques
        for i in range(0, self.trainingModel.lenSelectedPlate):
            checkButton = self.trainingView.checkPlateList[i]
            checkButton["text"] = self.trainingModel.selectedPlates[i].toString()
            # x=i car si i utilisé directement, il est mis en attente jusqu'à l'appel, et i fini = au dernier
            checkButton["command"] = lambda x=i: self.checkMaxOfPlate(x)
            checkButton["offvalue"] = -1
            checkButton.deselect()
            checkButton["onvalue"] = i

        # completion des checKButtons des plaques
        for i in range(0, self.operatorNumber):
            checkButton = self.trainingView.checkOperatorList[i]
            checkButton["text"] = self.operators[i]
            # x=i car si i utilisé directement, il est mis en attente jusqu'à l'appel, et i fini = au dernier
            checkButton["command"] = lambda x=i: self.checkMaxOfOperator(x)
            checkButton["offvalue"] = -1
            checkButton.deselect()
            checkButton["onvalue"] = i


    #Controle qu'il n'y a que 2 plaques selectionnées, sinon retire la plus anciennce
    def checkMaxOfPlate(self, pos):
        if self.firstPlate == pos :
            self.firstPlate = None
        elif self.secondPlate == pos :
            self.secondPlate = None
        elif self.firstPlate == None :
            self.firstPlate = pos
        elif self.secondPlate == None :
            self.secondPlate = pos
        else :
            self.trainingView.checkPlateList[self.secondPlate].deselect()
            self.secondPlate = self.firstPlate
            self.firstPlate = pos

    #Controle qu'il n'y a qu'une plaque de selectionnée, sinon la remplace
    def checkMaxOfOperator(self, pos):
        if self.operator == pos :
            self.operator == None
        elif self.operator == None :
            self.operator = pos
        else :
            self.trainingView.checkOperatorList[self.operator].deselect()
            self.operator = pos

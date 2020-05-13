import tkinter as tk

from Projet.Controller.playableController import PlayableController
from Projet.Model.trainingModel import TrainingModel
from Projet.Model.util import PLATE_NUMBER, OPERATORS, OPERATOR_NUMBER
from Projet.View.trainingView import TrainingView


class TrainingController(PlayableController):
    def __init__(self, parent, root):

        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER

        super(TrainingController, self).__init__(parent, TrainingModel(),
                                                 TrainingView(self.maxPlateNumber, OPERATOR_NUMBER, root))

        self.completeButton("Back Step", lambda: self.backStep(), self.view.backButton)
        self.completeButton("Back", lambda: self.backMenu(root), self.view.returnButton)
        self.completeButton("New One", lambda: self.newOne(), self.view.newButton)
        self.completeButton("Solution ?", lambda: self.getSolution(root), self.view.solutionButton)

        self.updateView()

    def getSolution(self, root):
        self.view.displayInfo("Please wait, Daisy heard your request...\n"
                              "Just let her some time to think about it...")
        root.update()
        operations, difference = self.model.findSolution()
        self.view.displayInfo("The best is a difference of " +
                              str(difference) +
                              "\nwith " + str(operations).replace('(', '').replace(')', '')
                              + " from left to right")

    def newOne(self):
        self.view.displayInfo()
        self.view.showAllPlateButtons()
        self.model = TrainingModel()
        self.updateView()

    def backStep(self):
        if len(self.model.history) > 0:
            self.view.showHidePlateButton(self.model.lenSelectedPlate, 1)
            self.model.previousHistory()
            self.updateView()
            self.view.displayInfo()
        else:
            self.view.displayInfo("History empty, please play before")

    def backMenu(self, root):
        root.destroy()
        root = tk.Tk()
        self.parent.__init__(root)
        root.mainloop()

    def completeButton(self, text, fct, button):
        button["text"] = text
        button["command"] = fct

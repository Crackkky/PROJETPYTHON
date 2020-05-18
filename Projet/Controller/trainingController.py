import tkinter as tk

from Projet.Controller.playableController import PlayableController
from Projet.Model.trainingModel import TrainingModel
from Projet.View.trainingView import TrainingView


class TrainingController(PlayableController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxTileNumber = TILE_NUMBER

        super(TrainingController, self).__init__(parent, TrainingModel(),
                                                 TrainingView(self.maxTileNumber, self.operatorNumber, root), self.operators)

        self.completeButton("Back Step", lambda: self.backStep(), self.view.backButton)
        self.completeButton("Back", lambda: self.backMenu(root), self.view.returnButton)
        self.completeButton("New One", lambda: self.newOne(), self.view.newButton)
        self.completeButton("Solution ?", lambda: self.getSolution(root), self.view.solutionButton)

        self.updateView()
        self.view.hideShowGame(1)

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
        self.view.showHideAllTileButtons(1)
        self.model = TrainingModel()
        self.updateView()

    def backStep(self):
        if len(self.model.history) > 0:
            self.view.showHideTileButton(self.model.lenSelectedTile, 1)
            self.model.previousHistory()
            self.updateView()
            self.view.displayInfo()
        else:
            self.view.displayInfo("History empty, please play before")

    def updateView(self):
        super(TrainingController, self).updateView()
        self.view.historyLabel["text"] = "History" + self.model.historyToString()

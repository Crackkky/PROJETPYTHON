import time
from tkinter import StringVar

from Projet.Controller.playableController import PlayableController
from Projet.Model.onlineModel import OnlineModel
from Projet.Model.util import DEFAULT_TIME
from Projet.View.plateView import PlateView


class OnlineController(PlayableController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, model=None, view=None, ivyObject=None):
        if view is None:
            view = PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root)
        if model is None:
            model = OnlineModel()
        super(OnlineController, self).__init__(parent, model, view, OPERATORS)
        self.parent = parent
        self.root = root
        self.plateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        self.maxTimer = 2
        self.beginTime = None
        self.gotTime = None
        self.stillTrying = None
        self.differenceSaid = StringVar()
        self.view.differenceEntry["textvariable"] = self.differenceSaid
        self.view.hideShowGame(1)
        self.play()

    def found(self):
        self.view.hideShowGame(1)
        self.stillTrying = False
        self.model.found()
        self.view.displayInfo("Please, play without any mistake")
        self.completeButton("Validate", lambda: self.validate(), self.view.validateButton)

    def done(self):
        difference = self.model.getDifference()
        if difference != 0:
            point = 1  # point for opponent
        else:
            point = 0  # point for me
        self.model.pointSetter(point)
        self.model.countScore(point)
        self.view.displayInfo("Point for " + ("you, Lisa would be proud !" if point == 0 else "opponent, mensongeur !"))
        self.completeButton("Play Again", lambda: self.playAgain(), self.view.validateButton)

    def checkOpponent(self):
        if self.model.isFound():
            self.stillTrying = False
            self.checkPoint()
        else:
            self.root.after(100, lambda: self.checkOpponent())

    def checkUpdateTimer(self):
        if self.stillTrying:
            self.gotTime = self.beginTime + self.maxTimer - time.time()
            if self.gotTime < 0:
                self.stillTrying = False
                self.view.hideShowGame(0)
                self.view.displayInfo("Please, what is your closest result ?")
                self.differenceSaid.set("")
                self.view.hideShowEntry(1)
                self.completeButton("Done", lambda :self.wroteDifference(), self.view.validateButton)
                self.view.hideShowValidate(1)
                self.ivyObject.clearMessages()
            else:
                self.view.timeLabel["text"] = "Time : " + str(int(self.gotTime))
                self.root.after(100, lambda: self.checkUpdateTimer())

    def wroteDifference(self):
        if self.model.isInteger(self.differenceSaid.get()):
            self.view.displayInfo("Waiting for opponent...")
            self.view.hideShowEntry(0)
            self.view.hideShowGame(0)
            self.root.update()
            if self.model.isServer():
                self.launchSecondRound()
            else:
                self.sendDifference()
        else:
            self.view.displayInfo("Enter the closest Integer you found.")


    def playerInit(self, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject, root):
        self.view.scoreLabel["text"] = self.model.getScoreString()
        self.stillTrying = True
        self.beginTime = time.time()
        self.checkUpdateTimer()
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        self.completeButton("back", lambda: self.backMenu(root), self.view.returnButton)
        self.completeButton("Got It !", lambda: self.found(), self.view.validateButton)
        self.view.hideShowGame(1)
        self.updateView()

    def checkPoint(self):
        self.view.hideShowGame(0)
        self.view.displayInfo("Waiting for opponent's solution")
        self.root.update()
        point = self.model.pointGetter()
        while not point:
            point = self.model.pointGetter()
        self.model.countScore(1 - point)
        self.view.displayInfo("Got the point " + str(point))
        self.view.hideShowGame(1)
        self.completeButton("Play Again", lambda: self.playAgain(), self.view.validateButton)

    def playAgain(self):
        self.view.hideShowGame(0)
        self.view.displayInfo("Waiting for opponent's choice")
        again = self.model.doWePlayAgain()
        self.root.update()
        self.model.ready()
        while not again:
            again = self.model.doWePlayAgain()
        self.model.ready()
        self.play()
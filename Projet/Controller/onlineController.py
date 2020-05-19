import time
from tkinter import StringVar

from Projet.Controller.playableController import PlayableController
from Projet.Model.onlineModel import OnlineModel
from Projet.Model.util import DEFAULT_TIME
from Projet.View.tileView import TileView


class OnlineController(PlayableController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER, backMenuFct, model=None, view=None, ivyObject=None):
        if view is None:
            view = TileView(TILE_NUMBER, OPERATOR_NUMBER, root)
        if model is None:
            model = OnlineModel()
        super(OnlineController, self).__init__(parent, model, view, OPERATORS)
        self.parent = parent
        self.root = root
        self.tileNumber = TILE_NUMBER
        self.ivyObject = ivyObject
        self.backMenuFct = backMenuFct
        self.maxTimer = 5
        self.bothPlay = False
        self.pointSeparate = False
        self.wonPoint = False
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
        self.view.hideShowReturnButton(0)
        self.updateView()
        self.root.update()


    def done(self):
        difference = self.model.getDifference()
        if difference != 0:
            point = 1  # point for opponent
        else:
            point = 0  # point for me
        time.sleep(0.01)
        self.model.pointSetter(point)
        if (self.pointSeparate and point is 0) or self.pointSeparate is False:
            self.wonPoint = self.model.countScore(point, self.wonPoint)
        if self.bothPlay:
            self.bothPlay = False
            self.checkPoint()
        else:
            self.view.displayInfo("Point for you, Lisa would be proud !" if self.wonPoint else "Oh really ! Its so bad, maybe next time ? ")
            self.completeButton("Play Again", lambda: self.playAgain(), self.view.validateButton)
            self.view.hideShowReturnButton(1)
            self.ivyObject.clearMessages()

    def checkOpponent(self):
        if self.model.isFound():
            self.stillTrying = False
            self.checkPoint()
        elif self.stillTrying:
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
                self.completeButton("Done", lambda: self.wroteDifference(), self.view.validateButton)
                self.view.hideShowValidate(1)
            else:
                self.view.timeLabel["text"] = "Time : " + str(int(self.gotTime))
                self.root.after(10, lambda: self.checkUpdateTimer())

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
            self.view.displayInfo(
                "Enter an Integer inf to" + str(self.model.min_goal) + " and sup to " + str(self.model.max_goal))

    def playerInit(self, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER, ivyObject, root):
        self.view.scoreLabel["text"] = self.model.getScoreString()
        self.stillTrying = True
        self.bothPlay = False
        self.pointSeparate = False
        self.wonPoint = False
        self.beginTime = time.time()
        self.checkUpdateTimer()
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxTileNumber = TILE_NUMBER
        self.ivyObject = ivyObject
        self.completeButton("Back", lambda x=self.root:self.backMenuFct(x), self.view.returnButton)
        self.completeButton("Got It !", lambda: self.found(), self.view.validateButton)
        self.view.hideShowGame(1)
        self.view.hideShowReturnButton(0)
        self.updateView()

    def checkPoint(self):
        self.view.hideShowGame(0)
        self.view.displayInfo("Waiting for opponent's solution")
        self.root.update()
        self.getPointFromOpponent()

    def getPointFromOpponent(self):
        point = self.model.pointGetter()
        if point is "":
            self.root.after(1, lambda: self.getPointFromOpponent())
        else:
            if (self.pointSeparate and point is 0) or self.pointSeparate is False:
                self.wonPoint = self.model.countScore(1-point, self.wonPoint)
            if not self.wonPoint:
                self.view.displayInfo("Arg so bad, maybe next time ?")
            else:
                self.view.displayInfo("You got a point, yay ! Good job bro !")
            self.view.hideShowGame(1)
            self.completeButton("Play Again", lambda: self.playAgain(), self.view.validateButton)
            self.view.hideShowReturnButton(1)
            self.updateView()
            if self.bothPlay:
                self.bothPlay = False
                self.found()

    def playAgain(self):
        self.view.hideShowGame(0)
        self.view.displayInfo("Waiting for opponent's choice")
        self.root.update()
        # self.waitPlayAgainOpponent() #pas necessaire finalement
        self.play()

    def waitPlayAgainOpponent(self):
        again = self.model.doWePlayAgain()
        self.model.ready()
        if not again:
            self.root.after(100, lambda: self.waitPlayAgainOpponent())
        else:
            self.play()
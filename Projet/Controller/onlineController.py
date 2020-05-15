from Projet.Controller.plateController import PlateController
from Projet.Controller.playableController import PlayableController
from Projet.Model.onlineModel import OnlineModel
from Projet.View.plateView import PlateView


class OnlineController(PlayableController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, model = None, view = None, ivyObject = None):
        if view is None:
            view = PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root)
        if model is None:
            model = OnlineModel()
        super(OnlineController, self).__init__(parent, model, view, OPERATORS)
        self.parent = parent
        self.root = root
        self.plateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject

    def found(self):
        self.model.found()
        self.view.displayInfo("Please, play without any mistake")
        self.completeButton("Validate", lambda :self.validate(), self.view.validateButton)

    def done(self):
        difference = self.model.getDifference()
        if difference is not 0:
            point = 1 #point for opponent
        else:
            point = 0 #point for me
        self.model.pointSetter(point)
        self.model.countScore(point)
        self.view.displayInfo("Point for " + ("you, Lisa would be proud !" if point is 0 else "opponent, mensongeur !"))
        self.completeButton("Play Again", lambda: self.playAgain(), self.view.validateButton)

    def checkOpponent(self):
        if self.model.isFound():
            self.checkPoint()
        else:
            self.root.after(100, lambda: self.checkOpponent())

    def playerInit(self, OPERATORS,OPERATOR_NUMBER,PLATE_NUMBER,ivyObject, root):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        self.completeButton("back", lambda: self.backMenu(root), self.view.returnButton)
        self.completeButton("Got It !", lambda: self.found(), self.view.validateButton)
        self.updateView()

    def checkPoint(self):
        self.view.hideShowGame(0)
        self.view.displayInfo("Waiting for opponent's solution")
        self.root.update()
        point = self.model.pointGetter()
        while not point:
            point = self.model.pointGetter()
        self.model.countScore(1-point)
        self.view.displayInfo("Got the point " + str(point))
        self.view.hideShowGame(1)
        self.completeButton("Play Again", lambda:self.playAgain(), self.view.validateButton)

    def playAgain(self):
        self.model.ready()
        self.view.hideShowGame(0)
        self.view.displayInfo("Waiting for opponent's choice")
        again = self.model.doWePlayAgain()
        self.root.update()
        while not again:
            again = self.model.doWePlayAgain()
        self.play()
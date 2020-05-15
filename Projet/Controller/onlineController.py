from Projet.Controller.plateController import PlateController
from Projet.Model.onlineModel import OnlineModel
from Projet.View.plateView import PlateView


class OnlineController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, model = None, view = None):
        if view is None:
            view = PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root)
        if model is None:
            model = OnlineModel()
        super(OnlineController, self).__init__(parent, model, view, OPERATORS)
        self.parent = parent
        self.root = root
        self.plateNumber = PLATE_NUMBER

    def found(self):
        self.model.found()

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
        point = self.model.pointGetter()
        while not point :
            self.model.pointGetter()
        self.view.displayInfo("Got the point " + str(point))
        self.root.update()

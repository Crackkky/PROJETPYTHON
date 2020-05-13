from Projet.Controller.plateController import PlateController
from Projet.Model.plateModel import PlateModel
from Projet.View.plateView import PlateView


class OnlineServerController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        super(OnlineServerController, self).__init__(parent, PlateModel(),
                                               PlateView(self.maxPlateNumber, self.operatorNumber, root), OPERATORS)

        self.view.hideShowGame(0)
        self.view.displayInfo("Hi, we are the server")
        root.update()

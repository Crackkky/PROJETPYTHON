from Projet.Controller.plateController import PlateController
from Projet.Model.plateModel import PlateModel
from Projet.View.plateView import PlateView


class OnlineController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER

        super(OnlineController, self).__init__(parent, PlateModel(),
                                               PlateView(self.maxPlateNumber, self.operatorNumber, root))

        self.view.hideShowGame(0)

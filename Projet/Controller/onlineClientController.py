from Projet.Controller.plateController import PlateController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.plateView import PlateView


class OnlineClientController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        super(OnlineClientController, self).__init__(parent, OnlineClientModel(self.maxPlateNumber, self.ivyObject),
                                               PlateView(self.maxPlateNumber, self.operatorNumber, root), OPERATORS)
        self.model.receiveInfos()
        self.updateView()

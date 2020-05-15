from Projet.Controller.onlineController import OnlineController
from Projet.Controller.plateController import PlateController
from Projet.Model.onlineServerModel import OnlineServerModel
from Projet.Model.plateModel import PlateModel
from Projet.View.plateView import PlateView


class OnlineServerController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        super(OnlineServerController, self).__init__(parent, root, self.operators, self.operatorNumber,
                                                     self.maxPlateNumber,
                                                     OnlineServerModel(self.ivyObject),
                                                     PlateView(self.maxPlateNumber, self.operatorNumber, root))

        self.model.sendInfos()
        self.completeButton("back", lambda :self.backMenu(root), self.view.returnButton)
        self.completeButton("Got It !", lambda: self.found(), self.view.validateButton)
        self.updateView()

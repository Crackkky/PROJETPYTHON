from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.plateView import PlateView


class OnlineClientController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        self.ivyObject = ivyObject
        super(OnlineClientController, self).__init__(parent, root, self.operators, self.operatorNumber, self.maxPlateNumber ,OnlineClientModel(self.maxPlateNumber, self.ivyObject),
                                               PlateView(self.maxPlateNumber, self.operatorNumber, root))
        self.model.receiveInfos()
        self.completeButton("back", lambda :self.backMenu(root), self.view.returnButton)
        self.completeButton("Got It !", lambda: self.found(), self.view.validateButton)
        self.updateView()

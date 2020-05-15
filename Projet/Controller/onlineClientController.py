from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.plateView import PlateView


class OnlineClientController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):

        super(OnlineClientController, self)\
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER ,
                                                     OnlineClientModel(PLATE_NUMBER, ivyObject),
                                                     PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root), ivyObject)
        self.play()

    def play(self):
        self.model.waitForOpponent()
        self.model.receiveInfos()
        self.playerInit(self.operators,self.operatorNumber,self.plateNumber,self.ivyObject,self.root)
        self.view.displayInfo("Client")
        self.view.hideShowGame(1)
        self.checkOpponent()

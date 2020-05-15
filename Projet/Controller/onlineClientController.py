from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.plateView import PlateView


class OnlineClientController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):

        super(OnlineClientController, self)\
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER ,
                                                     OnlineClientModel(PLATE_NUMBER, ivyObject),
                                                     PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root))
        self.model.receiveInfos()
        self.playerInit(OPERATORS,OPERATOR_NUMBER,PLATE_NUMBER,ivyObject,root)
        self.view.displayInfo("Client")
        self.checkOpponent()


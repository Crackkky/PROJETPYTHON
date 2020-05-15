from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineServerModel import OnlineServerModel
from Projet.View.plateView import PlateView


class OnlineServerController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        super(OnlineServerController, self) \
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER,
                      OnlineServerModel(ivyObject),
                      PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root))
        self.model.initGame()
        self.model.sendInfos()
        self.playerInit(OPERATORS,OPERATOR_NUMBER,PLATE_NUMBER,ivyObject, root)
        self.view.displayInfo("Server")
        self.checkOpponent()

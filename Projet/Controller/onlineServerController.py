from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineServerModel import OnlineServerModel
from Projet.View.onlineView import OnlineView


class OnlineServerController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        super(OnlineServerController, self) \
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER,
                      OnlineServerModel(ivyObject),
                      OnlineView(PLATE_NUMBER, OPERATOR_NUMBER, root), ivyObject)
        self.play()

    def play(self):
        self.model.waitForOpponent()
        self.model.sendInfos()
        self.playerInit(self.operators, self.operatorNumber, self.plateNumber, self.ivyObject, self.root)
        self.view.displayInfo("Server")
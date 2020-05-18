from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineServerModel import OnlineServerModel
from Projet.View.onlineView import OnlineView


class OnlineServerController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):
        super(OnlineServerController, self) \
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER,
                      OnlineServerModel(ivyObject),
                      OnlineView(PLATE_NUMBER, OPERATOR_NUMBER, root), ivyObject)

    def play(self):
        self.ivyObject.clearMessages()
        self.model.waitForOpponent()
        self.model.sendInfos()
        self.playerInit(self.operators, self.operatorNumber, self.plateNumber, self.ivyObject, self.root)
        self.view.displayInfo("Server")

    def launchSecondRound(self):
        value = None
        while not value:
            value = self.model.getDiff()
        if value:
            clientValue = self.model.getDifference(int(value))
            serverValue = self.model.getDifference(int(self.differenceSaid.get()))
            if clientValue < serverValue:
                self.model.clientTurn()
                self.checkPoint()
            elif clientValue > serverValue:
                self.model.serverTurn()
                self.found()
        else:
            self.root.after(100, lambda :self.launchSecondRound())
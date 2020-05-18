import time

from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineServerModel import OnlineServerModel
from Projet.View.onlineView import OnlineView


class OnlineServerController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER, ivyObject):
        super(OnlineServerController, self) \
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER,
                      OnlineServerModel(ivyObject),
                      OnlineView(TILE_NUMBER, OPERATOR_NUMBER, root), ivyObject)

    def play(self):
        if not self.model.waitForOpponent():
            self.root.after(10, lambda :self.play())
        else:
            time.sleep(0.01)
            self.model.sendInfos()
            self.checkOpponent()
            self.playerInit(self.operators, self.operatorNumber, self.tileNumber, self.ivyObject, self.root)
            self.view.displayInfo("Server")

    def launchSecondRound(self):
        value = self.model.getDiff()
        if not self.model.isInteger(value):
            self.root.after(10, lambda :self.launchSecondRound())
        else:
            clientValue = self.model.getDifference(int(value))
            serverValue = self.model.getDifference(int(self.differenceSaid.get()))
            if clientValue < serverValue:
                self.model.clientTurn()
                self.checkPoint()
            elif clientValue > serverValue:
                self.model.serverTurn()
                self.found()

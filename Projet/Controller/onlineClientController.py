import time

from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.onlineView import OnlineView


class OnlineClientController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER, backMenuFct, ivyObject):

        super(OnlineClientController, self) \
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER, backMenuFct,
                      OnlineClientModel(TILE_NUMBER, ivyObject),
                      OnlineView(TILE_NUMBER, OPERATOR_NUMBER, root), ivyObject)
        self.root.title("Client")

    def play(self):
        if not self.model.waitForOpponent():
            self.model.ready()
            self.root.after(1, lambda: self.play())
        else:
            self.model.receiveInfos()
            self.playerInit(self.operators, self.operatorNumber, self.tileNumber, self.ivyObject, self.root)
            self.checkOpponent()

    def sendDifference(self):
        msg = self.model.getTurn()
        if not msg:
            self.model.sendDiff(self.differenceSaid.get())
            self.root.after(1, lambda: self.sendDifference())
        else:
            value = int(msg)
            if value is self.model.CLIENT:
                self.model.goal = int(self.differenceSaid.get())
                self.found()
            elif value is self.model.SERVER:
                self.checkPoint()
            else:
                self.pointSeparate = True
                self.bothPlay = True
                self.model.goal = int(self.differenceSaid.get())
                self.found()

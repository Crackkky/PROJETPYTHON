import time

from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.onlineView import OnlineView


class OnlineClientController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER, ivyObject):

        super(OnlineClientController, self)\
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER ,
                                                     OnlineClientModel(TILE_NUMBER, ivyObject),
                                                     OnlineView(TILE_NUMBER, OPERATOR_NUMBER, root), ivyObject)

    def play(self):
        if not self.model.waitForOpponent():
            self.model.ready()
            self.root.after(20, lambda :self.play())
        else:
            self.model.receiveInfos()
            self.checkOpponent()
            self.playerInit(self.operators,self.operatorNumber,self.tileNumber,self.ivyObject,self.root)
            self.view.displayInfo("Client")

    def sendDifference(self):
        msg = self.model.getTurn()
        if not self.model.isInteger(msg):
            self.model.sendDiff(self.differenceSaid.get())
            self.root.after(1, lambda :self.sendDifference())
        else:
            value = int(msg)
            if value is self.model.type:
                self.model.goal = int(self.differenceSaid.get())
                self.found()
            else:
                self.checkPoint()

import time

from Projet.Controller.onlineController import OnlineController
from Projet.Model.onlineClientModel import OnlineClientModel
from Projet.View.onlineView import OnlineView


class OnlineClientController(OnlineController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, ivyObject):

        super(OnlineClientController, self)\
            .__init__(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER ,
                                                     OnlineClientModel(PLATE_NUMBER, ivyObject),
                                                     OnlineView(PLATE_NUMBER, OPERATOR_NUMBER, root), ivyObject)

    def play(self):
        if not self.model.waitForOpponent():
            self.root.after(10, lambda :self.play())
        else:
            self.model.receiveInfos()
            self.checkOpponent()
            self.playerInit(self.operators,self.operatorNumber,self.plateNumber,self.ivyObject,self.root)
            self.view.displayInfo("Client")

    def sendDifference(self):
        msg = self.model.getTurn()
        if not self.model.isInteger(msg):
            self.model.sendDiff(self.differenceSaid.get())
            self.root.after(10, lambda :self.sendDifference())
        else:
            value = int(msg)
            if value is self.model.type:
                self.found()
            else:
                self.checkPoint()

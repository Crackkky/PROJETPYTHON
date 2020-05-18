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
        self.ivyObject.clearMessages()
        self.checkOpponent()
        self.model.waitForOpponent()
        self.model.receiveInfos()
        self.playerInit(self.operators,self.operatorNumber,self.plateNumber,self.ivyObject,self.root)
        self.view.displayInfo("Client")

    def sendDifference(self):
        self.model.sendDiff(self.differenceSaid.get())
        msg = self.model.getTurn()
        if not self.model.isInteger(msg):
            time.sleep(0.01)
            self.sendDifference()

        else:
            print("Le client est passé")
            value = int(msg)
            if value is self.model.type:
                self.found()
            else:
                self.checkPoint()

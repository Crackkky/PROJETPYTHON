import time

from Projet.Controller.plateController import PlateController
from Projet.Model.IvyProject import sendMessage
from Projet.Model.ivyUtils import connexionIvy, getMessage
from Projet.Model.plateModel import PlateModel
from Projet.View.plateView import PlateView


class OnlineController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER):

        self.operators = OPERATORS
        self.operatorNumber = OPERATOR_NUMBER
        self.maxPlateNumber = PLATE_NUMBER
        super(OnlineController, self).__init__(parent, PlateModel(),
                                               PlateView(self.maxPlateNumber, self.operatorNumber, root))

        # Connection part
        self.opponentName = "nbPlayer"
        self.serverBind = "(Jisoo says: .*)"
        self.clientBind = "(Lisa says: .*)"
        self.connectionRegex = self.opponentName + " says: (.*)"

        self.view.hideShowGame(0)
        self.view.displayInfo("Looking for an opponent...")
        root.update()

        self.ivyObject = connexionIvy(self.opponentName)
        time.sleep(1)
        message = getMessage(self.ivyObject, 'nbPlayer says: (.*)')
        # self.ivyObject.clearMessages()

        if not message:
            sendMessage('nbPlayer says: 1')
            self.ivyObject.bindIvy(self.serverBind)
            self.view.displayInfo("Looks like we are the server !")
            self.server()
        else:
            self.ivyObject.bindIvy(self.clientBind)
            self.view.displayInfo("Looks like we are the client !")
            self.client()

    def server(self):
        print("yo")

    def client(self):
        print("yo")

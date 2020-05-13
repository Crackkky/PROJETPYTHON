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

        #Connection part
        self.opponentName = "nbPlayer"
        self.serverTalk = "Lisa says:"
        self.clientTalk = "Jisoo says:"
        self.connectionRegex = self.opponentName + " says: (.*)"

        self.view.hideShowGame(0)
        self.view.displayInfo("Looking for an oppenent...")
        root.update()

        self.ivyObject = connexionIvy(self.opponentName)
        time.sleep(1)
        message = getMessage(self.ivyObject, self.connectionRegex)

        self.ivyObject.clearMessages()

        if not message:
            self.server()
        else:
            self.client()

    def server(self):
        ready = ""
        self.ivyObject.bindIvy('(' + self.clientTalk + ' .*)')
        while not ready:
            sendMessage('nbPlayer says: 1')
            ready = getMessage(self.ivyObject, self.clientTalk + ' ready(.*)')
            time.sleep(0.1)

        self.ivyObject.bindIvy(self.clientTalk)
        self.view.displayInfo("Looks like we are the server !")

    def client(self):
        self.ivyObject.bindIvy('(' + self.serverTalk + ' .*)')
        sendMessage(self.clientTalk + ' ready!')
        self.ivyObject.bindIvy(self.serverTalk)
        self.view.displayInfo("Looks like we are the client !")

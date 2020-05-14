import time

from Projet.Model.IvyProject import IvyModel
from Projet.Model.playableModel import PlayableModel, sendMessage


class OnlineModel(PlayableModel):
    def __init__(self):
        self.SERVER = 0
        self.CLIENT = 1
        self.type = None
        super(OnlineModel, self).__init__()
        self.opponentName = "nbPlayer"
        self.connectionRegex = self.opponentName + " says: (.*)"
        self.clientTalk = "Jisoo says:"
        self.serverTalk = "Lisa says:"
        self.goalRegex = self.serverTalk + " Goal is"
        self.plateRegex = self.serverTalk + " Plate is"
        self.start = self.serverTalk + " start!"
        self.ivyObject = None

    def connect(self):
        self.ivyObject = self.connexionIvy(self.opponentName)
        time.sleep(1)
        message = self.getMessage(self.ivyObject, self.connectionRegex)
        self.ivyObject.clearMessages()
        if not message:
            ready = ""
            self.ivyObject.bindIvy('(' + self.clientTalk + ' .*)')
            while not ready:
                sendMessage('nbPlayer says: 1')
                ready = self.getMessage(self.ivyObject, self.clientTalk + ' ready(.*)')
                time.sleep(0.1)
            self.ivyObject.bindIvy(self.clientTalk)
            self.type = self.SERVER
        else:
            self.ivyObject.bindIvy('(' + self.serverTalk + ' .*)')
            sendMessage(self.clientTalk + ' ready!')
            self.ivyObject.bindIvy(self.serverTalk)
            self.type = self.CLIENT
        return self.type

    # Return the message or "" else
    def parseMessages(self, msg, regex):
        import re
        res = ""

        regex_search = re.search(regex, msg)
        if regex_search:
            res = regex_search.group(1)

        return res

    # Parse a message if there is one, else return ""
    def getMessage(self, ivyObject, regex):
        message = ""
        if ivyObject.messages:
            message = ivyObject.messages.pop()[0]
        return self.parseMessages(message, regex)

    # Create Ivy object and initialise a connexion
    def connexionIvy(self, opponentName):
        ivyObject = IvyModel('127.0.0.1:2487')
        ivyObject.bindIvy('(' + opponentName + ' says: .*)')
        time.sleep(0.1)
        return ivyObject
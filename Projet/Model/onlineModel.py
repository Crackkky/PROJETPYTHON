import time

from Projet.Model.ivyUtils import connexionIvy, getMessage
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
        self.ivyObject = None

    def connect(self):
        self.ivyObject = connexionIvy(self.opponentName)
        time.sleep(1)
        message = getMessage(self.ivyObject, self.connectionRegex)
        self.ivyObject.clearMessages()
        if not message:
            ready = ""
            self.ivyObject.bindIvy('(' + self.clientTalk + ' .*)')
            while not ready:
                sendMessage('nbPlayer says: 1')
                ready = getMessage(self.ivyObject, self.clientTalk + ' ready(.*)')
                time.sleep(0.1)
            self.ivyObject.bindIvy(self.clientTalk)
            self.type = self.SERVER
        else:
            self.ivyObject.bindIvy('(' + self.serverTalk + ' .*)')
            sendMessage(self.clientTalk + ' ready!')
            self.ivyObject.bindIvy(self.serverTalk)
            self.type = self.CLIENT
        return self.type

from Projet.Model.IvyProject import sendMessage
from Projet.Model.onlineModel import OnlineModel


class OnlineServerModel(OnlineModel):
    def __init__(self, ivyPlayer):
        super(OnlineServerModel, self).__init__()
        self.ivyObject = ivyPlayer

    def sendInfos(self):
        self.initGame()
        self.ivyObject.clearMessages()
        sendMessage(self.goalRegex + ' ' + str(self.goal))

        for i in range(0, len(self.selectedPlates)):
            sendMessage(self.plateRegex + ' ' + str(self.selectedPlates[i].getNumber()))
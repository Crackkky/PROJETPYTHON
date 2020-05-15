from Projet.Model.onlineModel import OnlineModel


class OnlineServerModel(OnlineModel):
    def __init__(self, ivyPlayer):
        super(OnlineServerModel, self).__init__()
        self.ivyObject = ivyPlayer
        self.write = self.serverTalk
        self.read = self.clientTalk

    def sendInfos(self):
        self.initGame()
        self.sendMsg(self.goalRegex + ' ' + str(self.goal))

        for i in range(0, len(self.selectedPlates)):
            self.sendMsg(self.plateRegex + ' ' + str(self.selectedPlates[i].getNumber()))

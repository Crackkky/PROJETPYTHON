from Projet.Model.onlineModel import OnlineModel


class OnlineServerModel(OnlineModel):
    def __init__(self, ivyPlayer):
        super(OnlineServerModel, self).__init__()
        self.ivyObject = ivyPlayer
        self.write = self.serverTalk
        self.read = self.clientTalk

    def sendInfos(self):
        self.initGame()
        self.type = self.SERVER
        self.sendMsg(self.goalRegex + ' ' + str(self.goal))

        for i in range(0, len(self.selectedPlates)):
            self.sendMsg(self.plateRegex + ' ' + str(self.selectedPlates[i].getNumber()))

    def clientTurn(self):
        self.sendMsg(self.play+str(self.CLIENT))

    def serverTurn(self):
        self.sendMsg(self.play+str(self.SERVER))

    def getDiff(self):
        return self.getMsg(self.diff+'(.*)')
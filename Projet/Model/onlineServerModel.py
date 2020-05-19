from Projet.Model.onlineModel import OnlineModel


class OnlineServerModel(OnlineModel):
    def __init__(self, ivyPlayer):
        super(OnlineServerModel, self).__init__()
        self.ivyObject = ivyPlayer
        self.write = self.serverTalk
        self.read = self.clientTalk

    # Send the informations (goal, tile array)
    def sendInfos(self):
        self.initGame()
        self.type = self.SERVER
        self.sendMsg(self.goalRegex + ' ' + str(self.goal))

        for i in range(0, len(self.selectedTiles)):
            self.sendMsg(self.tileRegex + ' ' + str(self.selectedTiles[i].getNumber()))

    # Send a message to tell the player it's his turn to suggest a solution
    def clientTurn(self):
        self.sendMsg(self.play + str(self.CLIENT))

    # Send a message to tell it's the server turn to suggest a solution
    def serverTurn(self):
        self.sendMsg(self.play + str(self.SERVER))

    # Send a message to tell that both player found a solution with the same difference
    def bothTurn(self):
        self.sendMsg(self.play + str(self.BOTH))

    # Get the opponent difference (when time is up)
    def getDiff(self):
        return self.getMsg(self.diff + '(.*)')

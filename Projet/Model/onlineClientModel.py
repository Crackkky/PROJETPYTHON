import time

from Projet.Model.onlineModel import OnlineModel
from Projet.Model.tile import Tile
from Projet.Model.util import POSSIBLE_TILES, MIN_GOAL, MAX_GOAL


class OnlineClientModel(OnlineModel):
    def __init__(self, maxTileNumber, ivyPlayer):
        super(OnlineClientModel, self).__init__()
        self.tileNumber = maxTileNumber
        self.possibleTiles = POSSIBLE_TILES
        self.ivyObject = ivyPlayer
        self.write = self.clientTalk
        self.read = self.serverTalk

    def receiveInfos(self):
        self.empty()
        self.type = self.CLIENT
        while self.goal is None or len(self.selectedTiles) < self.tileNumber:
            message = self.getMsgWithoutParse()
            goalTemp = self.parseMessages(message, self.goalRegex + ' (.*)')

            if goalTemp:
                self.goal = int(goalTemp)

            tile = self.parseMessages(message, self.tileRegex + ' (.*)')
            if tile and int(tile) in self.possibleTiles:
                self.selectedTiles.append(Tile(int(tile)))

            time.sleep(0.01)
        self.lenSelectedTile = len(self.selectedTiles)
        return self.goal, self.selectedTiles

    def sendDiff(self, diff):
        self.sendMsg(self.diff + diff)

    def getTurn(self):
        return self.getMsg(self.play+"(.*)")
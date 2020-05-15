import time

from Projet.Model.onlineModel import OnlineModel
from Projet.Model.plate import Plate
from Projet.Model.util import POSSIBLE_PLATES, MIN_GOAL, MAX_GOAL


class OnlineClientModel(OnlineModel):
    def __init__(self, maxPlateNumber, ivyPlayer):
        super(OnlineClientModel, self).__init__()
        self.plateNumber = maxPlateNumber
        self.possiblePlates = POSSIBLE_PLATES
        self.ivyObject = ivyPlayer
        self.min_goal = MIN_GOAL
        self.max_goal = MAX_GOAL
        self.write = self.clientTalk
        self.read = self.serverTalk

    def receiveInfos(self):
        while self.goal is None or len(self.selectedPlates) < self.plateNumber:
            message = self.getMsgWithoutParse()
            goalTemp = self.parseMessages(message, self.goalRegex + ' (.*)')

            if goalTemp and self.min_goal <= int(goalTemp) <= self.max_goal:
                self.goal = int(goalTemp)

            plate = self.parseMessages(message, self.plateRegex + ' (.*)')
            if plate and int(plate) in self.possiblePlates:
                self.selectedPlates.append(Plate(int(plate)))

            time.sleep(0.01)
        self.lenSelectedPlate = len(self.selectedPlates)
        return self.goal, self.selectedPlates

import time

from Projet.Model.onlineModel import OnlineModel
from Projet.Model.plate import Plate
from Projet.Model.util import POSSIBLE_PLATES, MIN_GOAL, MAX_GOAL


class OnlineClientModel(OnlineModel):
    def __init__(self, maxPlateNumber, ivyPlayer):
        super(OnlineClientModel, self).__init__()
        self.plateNumber = maxPlateNumber
        self.possibiblePlates = POSSIBLE_PLATES
        self.ivyObject = ivyPlayer
        self.min_goal = MIN_GOAL
        self.max_goal = MAX_GOAL

    def receiveInfos(self):
        while self.goal == 0 or len(self.selectedPlates) < self.plateNumber:
            if self.ivyObject.messages:
                message = self.ivyObject.messages.pop()[0]
                goalTemp = self.parseMessages(message, self.goalRegex + ' (.*)')

                if goalTemp and self.min_goal <= int(goalTemp) <= self.max_goal:
                    goal = int(goalTemp)
                    message = ""

                plate = self.parseMessages(message, self.plateRegex + ' (.*)')
                if plate and int(plate) in self.possiblePlates:
                    self.selectedPlates.append(Plate(int(plate)))
                    message = ""

                m = self.parseMessages(message, self.serverTalk + ' (.*)')
                if m:
                    message = ""

            time.sleep(0.01)

        return self.goal, self.selectedPlates

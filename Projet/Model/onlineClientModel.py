from Projet.Model.onlineModel import OnlineModel


class OnlineClientModel(OnlineModel):
    def __init__(self):
        super(OnlineClientModel, self).__init__()

    def receiveInfos(ivyPlayer):
        while goal == 0 or len(self.selectedPlates) < PLATE_NUMBER:
            if ivyPlayer.messages:
                message = ivyPlayer.messages.pop()[0]

            goalTemp = parseMessages(message, 'Lisa says: Goal is (.*)')
            if goalTemp and 100 <= int(goalTemp) <= 999:
                goal = int(goalTemp)
                # print('GOAL IS :', goal)
                message = ""

            plate = parseMessages(message, 'Lisa says: Plate is (.*)')
            if plate and int(plate) in possiblePlates:
                selectedPlates.append(Plate(int(plate)))
                # print('PLATE IS :', plate)
                message = ""

            m = parseMessages(message, 'Lisa says: (.*)')
            if m:
                message = ""

            time.sleep(0.01)

        return goal, selectedPlates
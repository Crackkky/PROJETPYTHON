from Projet.Model.IvyProject import *
from Projet.Model.training import *
import Projet.Model.util as util
import time


def receiveInfos(ivyPlayer):  # TODO Improvable
    goal = 0
    selectedPlates = []
    possiblePlates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
    message = ""
    while goal == 0 or len(selectedPlates) < 6:  # TODO 6 durs
        time.sleep(0.005)
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

    return goal, selectedPlates


def playerMode():
    print('Welcome player !')

    # connexion au bus
    ivyPlayer = connexionIvy('Lisa')

    # recevoir les infos de Lisa
    goal, selectedPlates = receiveInfos(ivyPlayer)
    print('GOAL :')
    print(goal)
    print('PLATES :')
    printArray(selectedPlates)

    # attendre signal serveur (Ou envoyer)
    while True:
        message = ""
        if ivyPlayer.messages:
            message = ivyPlayer.messages.pop()[0]
        if parseMessages(message, 'Lisa says: start(.*)'):
            print('MESSAGE :', message)

            # Start the game
            util.gameStart(ivyPlayer, goal, selectedPlates, 'Jisoo', 'Lisa')

    # Suggest a solution

    # selectedPlates = [Plate(2), Plate(4), Plate(25), Plate(1), Plate(75), Plate(8)]
    # history = []

    # print('Play again?')
    # yes = chooseYesNo()

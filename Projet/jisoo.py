from Projet.IvyProject import *
from Projet.training import *
import time


def parseMessages(msg, regex):
    import re
    res = ""

    regex_search = re.search(regex, msg)
    if regex_search:
        res = regex_search.group(1)
        # print('PARSED : \"' + res + '\"')

    return res


# 'Lisa says: (.*)'
def receiveInfos(ivyServer):
    goal = 0
    selectedPlates = []
    possiblePlates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
    message = ""
    while goal == 0 or len(selectedPlates) < 6:  # TODO 6 durs
        time.sleep(0.001)
        if ivyServer.messages:
            message = ivyServer.messages.pop()[0]

        goalTemp = parseMessages(message, 'Lisa says: Goal is (.*)')
        if goalTemp and 100 <= int(goalTemp) <= 999:
            goal = int(goalTemp)
            print('GOAL IS :', goal)
            message = ""

        plate = parseMessages(message, 'Lisa says: Plate is (.*)')
        if plate and int(plate) in possiblePlates:
            selectedPlates.append(Plate(int(plate)))
            print('PLATE IS :', plate)
            message = ""

        m = parseMessages(message, 'Lisa says: (.*)')
        if m:
            message = ""

    return goal, selectedPlates


def playerMode():
    print('Welcome player !')

    # connexion au bus
    ivyServer = IvyModel('127.0.0.1:2010')
    ivyServer.bindIvyPlayer('(Lisa says: .*)')
    time.sleep(1)

    # recevoir les infos de Lisa
    goal, selectedplates = receiveInfos(ivyServer)
    print('GOAL :')
    print(goal)
    print('PLATES :')
    printArray(selectedplates)

    # attendre signal serveur (Ou envoyer)
    # lancer la fonction "suggest solution"

    # selectedPlates = [Plate(2), Plate(4), Plate(25), Plate(1), Plate(75), Plate(8)]
    # history = []

    # print('Play again?')
    # yes = chooseYesNo()

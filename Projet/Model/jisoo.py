from Projet.Model.training import *
import Projet.Model.util as util
import time


def receiveInfos(ivyPlayer):  # TODO Improvable
    goal = 0
    selectedPlates = []
    possiblePlates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
    message = ""
    while goal == 0 or len(selectedPlates) < PLATE_NUMBER:
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


def playerMode(ivyPlayer):
    print('Welcome player !')

    # Connexion
    # ivyPlayer = connexionIvy('Lisa')
    # print('Connected!')

    print('Waiting for an opponent...')

    sendMessage('Jisoo says: ', 'ready!')
    print('SENT')

    ivyPlayer.clearMessages()
    play = True
    while play:
        # Wait for new game information
        print('Now waiting for game information...')
        goal, selectedPlates = receiveInfos(ivyPlayer)
        print('GOAL :')
        print(goal)
        print('PLATES :')
        printArray(selectedPlates)

        # Wait for the beginning of the game
        endOfTheGame = False
        oneFound = True
        while not endOfTheGame:
            message = getMessage(ivyPlayer, 'Lisa says: start(.*)')
            if message:
                # Start the game
                oneFound = util.gameStart(ivyPlayer, goal, selectedPlates, 'Jisoo', 'Lisa')
                endOfTheGame = True
            time.sleep(0.1)

        if not oneFound:
            print('YYYYYYYYY')

        # TODO /!\ input!!
        play = replayPlayer('Jisoo', 'Lisa', ivyPlayer)


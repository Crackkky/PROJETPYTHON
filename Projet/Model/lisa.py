from Projet.Model.IvyProject import *
from Projet.Model.training import *
import Projet.Model.util as util


def serverMode(ivyServer):
    print('Welcome mister server !')

    # Connexion
    # ivyServer = connexionIvy('Jisoo')

    print('Waiting for an opponent...')
    ready = ""
    while not ready:
        sendMessage('nbPlayer says:', ' 1')
        ready = getMessage(ivyServer, 'Jisoo says: ready(.*)')
        # print(ready)
        time.sleep(0.1)

    print('Opponent found!')
    print('Now loading...')
    print('')

    ivyServer.clearMessages()
    play = True
    while play:
        # Send informations to Jisoo
        goal, selectedPlates = generateGoalPlates(100, 999, 27)
        sendMessage('Lisa says: ', 'Goal is ' + str(goal))

        if len(selectedPlates) > 0:
            for i in range(0, len(selectedPlates)):
                sendMessage('Lisa says: ', 'Plate is ' + str(selectedPlates[i].getNumber()))
        else:
            print('Empty array!')

        print('GOAL :')
        print(goal)
        print('PLATES :')
        printArray(selectedPlates)

        # Start the game
        time.sleep(0.1)
        sendMessage('Lisa says: ', 'start!')

        if not util.gameStart(ivyServer,
                              goal,
                              selectedPlates,
                              'Lisa',
                              'Jisoo'):
            print('YYYYYYYYYYY')

        # TODO /!\ input!!
        play = replayServer('Lisa', 'Jisoo', ivyServer)

        time.sleep(1)

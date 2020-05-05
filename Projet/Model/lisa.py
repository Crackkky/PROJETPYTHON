from Projet.Model.IvyProject import *
from Projet.Model.training import *
import Projet.Model.util as util


def serverMode():
    print('Welcome mister server !')

    # Connexion
    ivyServer = connexionIvy('Jisoo')

    play = True
    endOfTheGame = False

    while play:
        # Send informations to Jisoo
        goal, selectedPlates = generateGoalPlates(100, 999, 27)
        sendMessage('Lisa says: ', 'Goal is ' + str(goal))

        if len(selectedPlates) > 0:
            for i in range(0, len(selectedPlates)):
                sendMessage('Lisa says: ', 'Plate is ' + str(selectedPlates[i].getNumber()))
            printArray(selectedPlates)
        else:
            print('Empty array!')

        # Start the game

        time.sleep(0.1)
        sendMessage('Lisa says: ', 'start!')

        util.gameStart(ivyServer, goal, selectedPlates, 'Lisa', 'Jisoo')

        print('Play again?')
        play = chooseYesNo()
        if not play:
            sendMessage('Lisa says: ', 'again not')
        else:
            sendMessage('Lisa says: ', 'again !')
            play = receivePlayAgain('Jisoo', ivyServer)
        print('OK let\'s play again')
        time.sleep(1)

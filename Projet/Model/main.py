from Projet.Model.jisoo import *
from Projet.Model.lisa import *
from Projet.Model.training import *


# FUNCTION DEF


def chooseMainMenu():
    while True:
        print('Choose an option:')
        print('0. Quit')
        print('1. Play in training')
        print('2. Play online!')
        index = int(input('(Enter the number) => '))
        if index > 2 or index < 0:
            print('Erreur Menu !')
        else:
            return index


def play():
    ivyObject = connexionIvy('nbPlayer')
    time.sleep(1)
    message = getMessage(ivyObject, 'nbPlayer says: (.*)')
    if not message:
        ivyObject.clearMessages()
        ivyObject.bindIvy('(Jisoo says: .*)')
        serverMode(ivyObject)
    else:
        ivyObject.clearMessages()
        ivyObject.bindIvy('(Lisa says: .*)')
        playerMode(ivyObject)

    nbPlayer = 0
    IvyStop()


# FUNCTION DEF

print('Welcome to : \" <Name of the game>\"!')

menuSelection = chooseMainMenu()

while True:

    if menuSelection == 1:
        trainingMode()
    if menuSelection == 2:
        play()
        print('Your score was:', scoreToString(True))
        print('Your Opponent\'s score was:', scoreToString(False))
    elif menuSelection == 0:
        print('\nYou\'ve chosen to quit, bye-bye ! ')
        sys.exit()

    menuSelection = chooseMainMenu()

from Projet.jisoo import *
from Projet.lisa import *
from Projet.training import *


# FUNCTION DEF


def chooseMainMenu():
    while True:
        print('Choose an option:')
        print('0. Quit')
        print('1. Play in training')
        print('2. Play as Lisa (Server)')
        print('3. Play as Jisoo (Player)')
        index = int(input('(Enter the number) => '))
        if index > 3 or index < 0:  # TODO 2 en durud
            print('Erreur Menu !')
        else:
            return index


# FUNCTION DEF

print('Welcome to : \" <Name of the game>\"!')

menuSelection = chooseMainMenu()

while menuSelection != 0:

    if menuSelection == 1:  # TODO dur?
        trainingMode()
    if menuSelection == 2:  # TODO dur?
        serverMode()
    if menuSelection == 3:  # TODO dur?
        playerMode()
    elif menuSelection == 0:  # TODO Durdur
        print('\nYou\'ve chosen to quit, bye-bye ! ')
        sys.exit()

    menuSelection = chooseMainMenu()












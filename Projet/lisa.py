import time

from Projet.IvyProject import *
from Projet.training import *


def suggestSolution(history, goal, selectedPlates):
    lenSelectedPlate = len(selectedPlates)
    while lenSelectedPlate != 1:
        while True:
            # Choose a plate
            print('You have : ')
            printArray(selectedPlates)
            print('You must find : ' + str(goal) + '\n')
            userSelections = chooseOperation(selectedPlates)

            # Do stuff with your plates
            try:
                operationFromArray(history, selectedPlates, userSelections[0], userSelections[1],
                                   userSelections[2])
                lenSelectedPlate = len(selectedPlates)
                break
            except Exception as e:
                print(e)
                printArray(selectedPlates)
            print('')

        print('______________________________________________________')
        print('')

    print('Your last plate is : ')
    printArray(selectedPlates)
    print('The goal was : ')
    print(goal)


def sendLisaMessage(msg):
    msg = 'Lisa says: ' + msg
    print('Sent :', msg)
    send_message(msg)


def serverMode():
    print('Welcome mister server !')

    # connexion au bus
    ivyServer = IvyModel('127.0.0.1:2010')
    ivyServer.bindIvyServer('(Jisoo says: .*)')
    time.sleep(1)
    goal, selectedPlates = generateGoalPlates(100, 999, 27)

    sendLisaMessage('Goal is ' + str(goal))

    if len(selectedPlates) > 0:
        for i in range(0, len(selectedPlates)):
            sendLisaMessage('Plate is ' + str(selectedPlates[i].getNumber()))
        printArray(selectedPlates)
    else:
        print('Empty array!')

    while True:
        # envoyer les info a Jisoo
        msg = input('Message a envoyer : ')
        sendLisaMessage(msg)

    # lancer le chrono + attendre un signal de la part du joueur
    # lancer la fonction "proposer solution"

    # selectedPlates = [Plate(2), Plate(4), Plate(25), Plate(1), Plate(75), Plate(8)]
    # history = []

    # suggestSolution(history, goal, selectedPlates)

    #  print('Play again?')
    #  yes = chooseYesNo()

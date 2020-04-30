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


def serverMode():
    print('Welcome mister server !')

    # connexion au bus
    goal, selectedPlates = generateGoalPlates(100, 999, 27)
    # envoyer les info a Jisoo
    # lancer le chrono + attendre un signal de la part du joueur
    # lancer la fonction "proposer solution"

    # selectedPlates = [Plate(2), Plate(4), Plate(25), Plate(1), Plate(75), Plate(8)]
    history = []

    suggestSolution(history, goal, selectedPlates)

    print('Play again?')
    yes = chooseYesNo()

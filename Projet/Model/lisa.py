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
        sendMessage('nbPlayer says: 1')
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
        # goal, selectedPlates = generateGoalPlates(100, 999, 27)

        goal, selectedPlates = 6, [Plate(1), Plate(1), Plate(1), Plate(1), Plate(1), Plate(1)]

        sendMessage('Lisa says: Goal is ' + str(goal))
        print('Lisa says: Goal is ' + str(goal))

        if len(selectedPlates) > 0:
            for i in range(0, len(selectedPlates)):
                sendMessage('Lisa says: Plate is ' + str(selectedPlates[i].getNumber()))
                print('Lisa says: Plate is ' + str(selectedPlates[i].getNumber()))
        else:
            print('Empty array!')

        print('GOAL :')
        print(goal)
        print('PLATES :')
        printArray(selectedPlates)

        # Start the game
        time.sleep(0.1)
        sendMessage('Lisa says: start!')

        if not util.gameStart(ivyServer,
                              goal,
                              selectedPlates,
                              'Lisa',
                              'Jisoo'):
            numberFound = int(input('What\'s the closest number you found?'))
            playerFound = ""
            while not playerFound:
                playerFound = getMessage(ivyServer, 'Jisoo says: found is (.*)')
                time.sleep(0.1)
            playerFound = int(playerFound)
            numberKept = closestNumber(numberFound, playerFound, goal)

            # DRAW
            if numberKept == -1:
                print('Both found')
                print('')
                sendMessage('Lisa says: found Both')
                if suggestSolution([], goal, selectedPlates) == numberFound:
                    sendMessage('Lisa says: answer = correct')
                    while True:
                        answerCorrect = getMessage(ivyServer, 'Jisoo says: answer = (.*)')
                        if answerCorrect == 'correct':  # TESTED
                            print('You both won !!!')
                            break
                        if answerCorrect == 'wrong':  # TESTED
                            print('Your opponent failed, you won !')
                            break
                        time.sleep(0.1)
                else:
                    sendMessage('Lisa says: answer = wrong')
                    while True:
                        answerCorrect = getMessage(ivyServer, 'Jisoo says: answer = (.*)')
                        if answerCorrect == 'correct':  # TESTED
                            print('Your opponent won !')
                            break
                        if answerCorrect == 'wrong':  # TESTED
                            print('You both failed !!!')
                            break
                        time.sleep(0.1)

            elif numberKept == numberFound:
                print('I found!')
                sendMessage('Lisa says: found I')
                answer = suggestSolution([], goal, selectedPlates)
                print('ANSWER :', answer)
                if answer == numberFound:  # TESTED
                    print('Correct !')
                    sendMessage('Lisa says: answer = correct')
                else:
                    print('Wrong !')  # TESTED
                    sendMessage('Lisa says: answer = wrong')

            elif numberKept == playerFound:
                sendMessage('Lisa says: found You')
                while True:
                    answer = getMessage(ivyServer, 'Jisoo says: answer = (.*)')
                    if answer == 'correct':  # TESTED
                        print('Your opponent found !')
                        break
                    elif answer == 'wrong':  # TESTED
                        print('Your opponent was wrong !')
                        break
                    time.sleep(0.1)

        play = replayServer('Lisa', 'Jisoo', ivyServer)

        time.sleep(1)

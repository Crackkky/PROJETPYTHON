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
        goal, selectedPlates = generateGoalPlates(100, 999, 27)

        # goal, selectedPlates = 2, [Plate(1), Plate(1)]

        sendMessage('Lisa says: Goal is ' + str(goal))

        if len(selectedPlates) > 0:
            for i in range(0, len(selectedPlates)):
                sendMessage('Lisa says: Plate is ' + str(selectedPlates[i].getNumber()))
        else:
            print('Empty array!')

        print('GOAL :')
        print(goal)
        print('PLATES :')
        printArray(selectedPlates)
        x = threading.Thread(target=thread_function)

        # Start the game
        time.sleep(0.1)
        sendMessage('Lisa says: start!')

        x.start()
        oneFound = util.gameStart(ivyServer, goal, selectedPlates, 'Lisa', 'Jisoo', 4)
        print('Enter anything to proceed : ')
        x.join()

        if not oneFound:  # Time's UP!
            print('Time\'s up!')
            numberFound = int(input('What\'s the closest number you found?'))
            playerFound = int(waitMessage(ivyServer, 'Jisoo says: found is (.*)'))
            numberKept = closestNumber(numberFound, playerFound, goal)

            # Lisa found!
            if numberKept == numberFound:
                print('I found!')
                sendMessage('Lisa says: found I')

                if numberFound == suggestSolution([], numberFound, selectedPlates):  # TESTED
                    print('Correct !')  # TESTED
                    scorePlusPlus(True)
                    sendMessage('Lisa says: answer = correct')
                else:
                    print('Wrong !')  # TESTED
                    scorePlusPlus(False)
                    sendMessage('Lisa says: answer = wrong')

            # Jisoo found!
            elif numberKept == playerFound:
                sendMessage('Lisa says: found You')
                print('Your opponent is closer!')
                answer = waitMessage(ivyServer, 'Jisoo says: answer = (.*)')

                if answer == 'correct':  # TESTED
                    print('Your opponent found !')
                    scorePlusPlus(False)
                elif answer == 'wrong':  # TESTED
                    print('Your opponent was wrong !')
                    scorePlusPlus(True)

            # Both found
            elif numberKept == -1:
                print('Both found')
                print('')
                sendMessage('Lisa says: found Both')

                # Lisa is correct
                if numberFound == suggestSolution([], numberFound, selectedPlates):
                    sendMessage('Lisa says: answer = correct')
                    answerCorrect = waitMessage(ivyServer, 'Jisoo says: answer = (.*)')

                    if answerCorrect == 'correct':  # TESTED
                        print('You both won !!!')
                        scorePlusPlus(True)
                        scorePlusPlus(False)
                    if answerCorrect == 'wrong':  # TESTED
                        print('Your opponent failed, you won !')
                        scorePlusPlus(True)
                # Lisa is wrong
                else:
                    sendMessage('Lisa says: answer = wrong')
                    answerCorrect = waitMessage(ivyServer, 'Jisoo says: answer = (.*)')

                    if answerCorrect == 'correct':  # TESTED
                        print('Your opponent won !')
                        scorePlusPlus(False)
                    if answerCorrect == 'wrong':  # TESTED
                        print('You both failed !!!')

        print('Your score was:', scoreToString(True))
        print('Your Opponent\'s score was:', scoreToString(False))
        play = replayServer('Lisa', 'Jisoo', ivyServer)

        time.sleep(1)

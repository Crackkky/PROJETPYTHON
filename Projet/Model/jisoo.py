from Projet.Model.training import *
import Projet.Model.util as util
import time


def receiveInfos(ivyPlayer):  # TODO Improvable
    goal = 0
    selectedTiles = []
    possibleTiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
    message = ""
    while goal == 0 or len(selectedTiles) < TILE_NUMBER:
        if ivyPlayer.messages:
            message = ivyPlayer.messages.pop()[0]

        goalTemp = parseMessages(message, 'Lisa says: Goal is (.*)')
        if goalTemp and 100 <= int(goalTemp) <= 999:
            goal = int(goalTemp)
            # print('GOAL IS :', goal)
            message = ""

        tile = parseMessages(message, 'Lisa says: Tile is (.*)')
        if tile and int(tile) in possibleTiles:
            selectedTiles.append(Tile(int(tile)))
            # print('TILE IS :', tile)
            message = ""

        m = parseMessages(message, 'Lisa says: (.*)')
        if m:
            message = ""

        time.sleep(0.01)

    return goal, selectedTiles


def playerMode(ivyPlayer):
    print('Welcome player !')

    # Connexion
    # ivyPlayer = connexionIvy('Lisa')
    # print('Connected!')

    print('Waiting for an opponent...')

    sendMessage('Jisoo says: ready!')

    ivyPlayer.clearMessages()
    play = True
    while play:
        # Wait for new game information
        print('Now waiting for game information...')
        goal, selectedTiles = receiveInfos(ivyPlayer)
        print('GOAL :')
        print(goal)
        print('TILES :')
        printArray(selectedTiles)

        # Wait for the beginning of the game
        endOfTheGame = False
        oneFound = True
        x = threading.Thread(target=thread_function)
        while not endOfTheGame:
            message = getMessage(ivyPlayer, 'Lisa says: start(.*)')
            if message:
                # Start the game
                x.start()
                oneFound = util.gameStart(ivyPlayer,
                                          goal,
                                          selectedTiles,
                                          'Jisoo',
                                          'Lisa',
                                          4)
                endOfTheGame = True
            time.sleep(0.1)
        print('Enter anything to proceed : ')
        x.join()

        if not oneFound:
            print('No one found in time!')
            print('')
            numberFound = int(input('What\'s the closest number you found?'))
            sendMessage('Jisoo says: found is ' + str(numberFound))

            message = waitMessage(ivyPlayer, 'Lisa says: found (.*)')
            if message == 'You':
                print('I found')
                if numberFound == suggestSolution([], numberFound, selectedTiles):  # TESTED
                    print('Correct !')
                    scorePlusPlus(True)
                    sendMessage('Jisoo says: answer = correct')
                else:
                    print('Wrong !')  # TESTED
                    scorePlusPlus(False)
                    sendMessage('Jisoo says: answer = wrong')

            elif message == 'I':
                print('Your opponent is closer!')
                answerCorrect = waitMessage(ivyPlayer, 'Lisa says: answer = (.*)')
                if answerCorrect == 'correct':  # TESTED
                    print('Your opponent won !')
                    scorePlusPlus(False)
                elif answerCorrect == 'wrong':  # TESTED
                    print('Your opponent was wrong !')
                    scorePlusPlus(True)

            elif message == 'Both':
                print('You both find the solution !')
                print('The server is proposing a solution...')
                answerCorrect = waitMessage(ivyPlayer, 'Lisa says: answer = (.*)')
                if answerCorrect == 'correct':
                    print('Your opponent found, your turn')
                    if numberFound == suggestSolution([], numberFound, selectedTiles):  # TESTED
                        print('You both won !!!')
                        scorePlusPlus(True)
                        scorePlusPlus(False)
                        sendMessage('Jisoo says: answer = correct')
                    else:  # TESTED
                        print('You failed, your opponent won !')
                        scorePlusPlus(False)
                        sendMessage('Jisoo says: answer = wrong')

                if answerCorrect == 'wrong':
                    print('Your opponent failed, your turn')
                    if numberFound == suggestSolution([], numberFound, selectedTiles):  # TESTED
                        print('You won !!!')
                        sendMessage('Jisoo says: answer = correct')
                        scorePlusPlus(True)
                    else:  # TESTED
                        print('You both failed !!!')
                        sendMessage('Jisoo says: answer = wrong')

        print('Your score was:', scoreToString(True))
        print('Your Opponent\'s score was:', scoreToString(False))
        play = replayPlayer('Jisoo', 'Lisa', ivyPlayer)

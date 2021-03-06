import time

from ivy.std_api import IvyStop

from Projet.Model.IvyModel import IvyModel
from Projet.Model.playableModel import PlayableModel, sendMessage
from Projet.Model.util import MIN_GOAL, MAX_GOAL


class OnlineModel(PlayableModel):
    def __init__(self):
        self.SERVER = 0
        self.CLIENT = 1
        self.BOTH = 2
        self.min_goal = MIN_GOAL
        self.max_goal = MAX_GOAL
        self.type = None
        self.ourScore = 0
        self.opponentScore = 0
        super(OnlineModel, self).__init__()
        self.opponentName = 'nbPlayer'
        self.clientTalk = 'Jisoo says:'
        self.serverTalk = 'Lisa says:'
        self.goalRegex = ' Goal is'
        self.tileRegex = ' Tile is'
        self.foundIt = ' found it '
        self.point = ' point '
        self.play = ' play'
        self.playAgain = " play again"
        self.diff = ' diff '
        self.stop = ' stop '
        self.ivyObject = None
        self.write = None
        self.read = None

    # Connexion des joueurs, le premier aura le comportement su serveur et l'autre du joueur
    def connect(self, leaveFunction):
        self.ivyObject = self.connexionIvy(self.opponentName, leaveFunction)
        time.sleep(1)
        message = self.getMsg(' says: (.*)', self.opponentName)
        if not message:
            self.type = self.SERVER
            ready = ""
            self.ivyObject.bindIvy('(' + self.clientTalk + ' .*)')
            while not ready:
                self.sendMsg(' 1', 'nbPlayer says:')
                ready = self.getMsg(' ready(.*)', self.clientTalk)
                time.sleep(0.01)
            self.ivyObject.bindIvy(self.clientTalk)
        else:
            self.type = self.CLIENT
            self.ivyObject.bindIvy('(' + self.serverTalk + ' .*)')
            self.sendMsg(' ready!', self.clientTalk)
            self.ivyObject.bindIvy(self.serverTalk)
        return self.type

    # Return the message or "" else
    def parseMessages(self, msg, regex):
        import re
        res = ""

        regex_search = re.search(regex, msg)
        if regex_search:
            res = regex_search.group(1)

        return res

    # Return the message if there is one, else return ""
    def getMsgWithoutParse(self):
        if self.ivyObject.messages:
            return self.ivyObject.messages.pop()[0]
        return ""

    # Parse a message if there is one, else return ""
    def getMsg(self, regex, opponentBind=None):
        if opponentBind is None:
            opponentBind = self.read
        message = self.getMsgWithoutParse()
        return self.parseMessages(message, opponentBind + regex)

    # Create Ivy object and initialise a connexion
    def connexionIvy(self, opponentName, leaveFunction):
        ivyObject = IvyModel('127.0.0.1:2487', leaveFunction)
        ivyObject.bindIvy('(' + opponentName + ' says: .*)')
        time.sleep(0.01)
        return ivyObject

    # Send a formated message
    def sendMsg(self, msg, mybind=None):
        if mybind is None:
            mybind = self.write
        sendMessage(mybind + msg)

    # Send a "found" message (used when someone find the solution before the end of the time)
    def found(self):
        self.sendMsg(self.foundIt + "!")

    # Test if the opponent found the solution
    def isFound(self):
        msg = self.getMsg(self.foundIt + '(.*)')
        return True if msg else False

    # Get the score
    def pointGetter(self):
        msg = self.getMsg(self.point + "(.*)")
        if msg:
            return int(msg)
        return msg

    # True if point for oppenent
    def pointSetter(self, loose):
        self.sendMsg(self.point + str(loose))

    # Add or substract the score
    def countScore(self, loose, wonAPoint):
        if loose is not None:
            self.ourScore += 1 - loose
            self.opponentScore += loose
        if not wonAPoint and loose is 1:
            return False
        return True

    # Function to test if both player want to play again
    def doWePlayAgain(self):
        msg = self.getMsg(self.stop + '(.*)')
        if not msg:
            return False
        else:
            return True

    # Send a "ready" message (used when the connexion is made)
    def ready(self):
        self.sendMsg(self.stop + ' No')

    # Quit the game
    def stopPlay(self):
        self.ivyObject.clearMessages()
        IvyStop()

    # Wait an opponent
    def waitForOpponent(self):
        self.sendMsg(' ready!')
        ready = self.getMsg(' ready(.*)')
        return ready

    # Get the score in a string
    def getScoreString(self):
        return "Score :\n" + "You : " + str(self.ourScore) + "\n" + "Other :" + str(self.opponentScore)

    # Test if value is an Integer
    def isInteger(self, value):
        try:
            return True if self.min_goal <= int(value) <= self.max_goal else False
        except ValueError:
            return False

    # Test if self is a server or a player
    def isServer(self):
        return self.type is self.SERVER

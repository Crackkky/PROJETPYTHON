import time

from Projet.Model.IvyModel import IvyModel
from Projet.Model.playableModel import PlayableModel, sendMessage


class OnlineModel(PlayableModel):
    def __init__(self):
        self.SERVER = 0
        self.CLIENT = 1
        self.BOTH = 2
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

    def connect(self):
        self.ivyObject = self.connexionIvy(self.opponentName)
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
    def connexionIvy(self, opponentName):
        ivyObject = IvyModel('127.0.0.1:2487')
        ivyObject.bindIvy('(' + opponentName + ' says: .*)')
        time.sleep(0.01)
        return ivyObject

    def sendMsg(self, msg, mybind=None):
        if mybind is None:
            mybind = self.write
        sendMessage(mybind + msg)

    def found(self):
        self.sendMsg(self.foundIt+"!")

    def isFound(self):
        msg = self.getMsg(self.foundIt+'(.*)')
        return True if msg else False

    def pointGetter(self):
        msg = self.getMsg(self.point+"(.*)")
        if msg :
            return int(msg)
        return msg

    #True if point for oppenent
    def pointSetter(self, loose):
        self.sendMsg(self.point+str(loose))

    #True if point for opponent
    def countScore(self, loose):
        if loose is not None:
            self.ourScore+=1-loose
            self.opponentScore+=loose

    def doWePlayAgain(self):
        msg = self.getMsg(self.stop + '(.*)')
        if not msg :
            return False
        else:
            return True

    def ready(self):
        self.sendMsg(self.stop + ' No')

    def waitForOpponent(self):
        self.sendMsg(' ready!')
        ready = self.getMsg(' ready(.*)')
        return ready

    def getScoreString(self):
        return "Score :\n"+ "You : " + str(self.ourScore) +"\n" + "Other :" + str(self.opponentScore)

    def isInteger(self, value):
        try:
            return True if int(value) >= 0 else False
        except ValueError:
            return False

    def isServer(self):
        return self.type is self.SERVER
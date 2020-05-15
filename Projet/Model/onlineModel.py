import time

from Projet.Model.IvyProject import IvyModel
from Projet.Model.playableModel import PlayableModel, sendMessage


class OnlineModel(PlayableModel):
    def __init__(self):
        self.SERVER = 0
        self.CLIENT = 1
        self.type = None
        self.ourScore = 0
        self.opponentScore = 0
        super(OnlineModel, self).__init__()
        self.opponentName = 'nbPlayer'
        self.clientTalk = 'Jisoo says:'
        self.serverTalk = 'Lisa says:'
        self.goalRegex = ' Goal is'
        self.plateRegex = ' Plate is'
        self.foundIt = ' found it'
        self.point = ' point '
        self.play = ' play'
        self.stop = ' make stop'
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
                time.sleep(0.1)
            self.ivyObject.bindIvy(self.clientTalk)
            # self.view.clearMessages()
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
        time.sleep(0.1)
        return ivyObject

    def sendMsg(self, msg, mybind=None):
        if mybind is None:
            mybind = self.write
        sendMessage(mybind + msg)

    def found(self):
        self.sendMsg(self.foundIt)

    def isFound(self):
        return True if (self.getMsg('(.*)') == self.foundIt) else False

    def pointGetter(self):
        msg = self.getMsg(self.point + ' (.*)')
        if msg :
            return int(msg)
        return msg

    #True if point for oppenent
    def pointSetter(self, loose):
        self.sendMsg(self.point + ' '+ str(loose))

    #True if point for opponent
    def countScore(self, loose):
        self.ourScore+=1-loose
        self.opponentScore+=loose

    def doWePlayAgain(self):
        msg = self.getMsg(self.play + '(.*)')
        if not msg :
            return False
        else:
            return True

    def ready(self):
        self.sendMsg(self.play + ' OK')

    def waitForOpponent(self):
        ready = False
        while not ready:
            self.sendMsg(' ready!')
            ready = self.getMsg(' ready(.*)')
            time.sleep(0.1)
from ivy.std_api import *

IvyServer = None
leaveFunction = None


# Défini un comportement en cas de demande de déconnexion
def on_die(agent, id):
    print('Received the order to die from %r with id = %d', agent, id)
    IvyStop()


# Défini un comportement en cas d'un changement de connexion sur le bus
def on_connection_change(agent, event):
    global IvyServer
    if event == IvyApplicationDisconnected:
        # print('Someone\'s disconnected !')
        leaveFunction()
        # print('Ivy application %r has disconnected', agent)
    else:
        print('New user connected !')
        # print('Ivy application %r has connected', agent)
    # print('Ivy applications currently on the bus : %s', ','.join(IvyGetApplicationList()))


# Envoi un message
def sendMessage(msg):
    IvySendMsg(msg)


# Démarre une connexion Ivy
def initIvy(ip, anotherLeave):
    global IvyServer
    global leaveFunction
    if IvyServer is None:
        IvyInit('IvyThread', 'Started!', 0, on_connection_change, on_die)
        IvyServer = True
    leaveFunction = anotherLeave
    IvyStart(ip)


# Objet d'Ivy permettant de récupérer les messages
class IvyModel:
    def __init__(self, ip, anotherLeave):
        initIvy(ip, anotherLeave)
        self.messages = []

    # Défini un comportement en cas de réception d'un message
    def on_msg(self, agent, *arg):
        if len(arg) is not 0:
            self.messages.append(arg)

    # Bind d'Ivy
    def bindIvy(self, bind):
        IvyBindMsg(self.on_msg, bind)

    # Nettoie la liste des messages
    def clearMessages(self):
        self.messages.clear()

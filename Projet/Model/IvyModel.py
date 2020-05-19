from ivy.std_api import *

IvyServer = None
leaveFunction = None

def on_die(agent, id):
    print('Received the order to die from %r with id = %d', agent, id)
    IvyStop()


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


def sendMessage(msg):
    IvySendMsg(msg)


def initIvy(ip, anotherLeave):
    global IvyServer
    global leaveFunction
    if IvyServer is None:
        IvyInit('IvyThread', 'Started!', 0, on_connection_change, on_die)
        IvyServer = True
    leaveFunction = anotherLeave
    IvyStart(ip)


class IvyModel:
    def __init__(self, ip, anotherLeave):
        initIvy(ip, anotherLeave)
        self.messages = []

    def on_msg(self, agent, *arg):
        if len(arg) is not 0:
            self.messages.append(arg)

    def bindIvy(self, bind):
        IvyBindMsg(self.on_msg, bind)

    def clearMessages(self):
        self.messages.clear()

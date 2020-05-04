from ivy.std_api import *


def on_die(agent, id):
    print('Received the order to die from %r with id = %d', agent, id)
    IvyStop()


def on_connection_change(agent, event):
    if event == IvyApplicationDisconnected:
        print('Ivy application %r has disconnected', agent)
    else:
        print('Ivy application %r has connected', agent)
    print('Ivy applications currntly on the bus : %s', ','.join(IvyGetApplicationList()))


def send_message(msg):
    IvySendMsg(msg)


class IvyModel:

    def __init__(self, ip):
        self.initIvyGeneral(ip)
        self.messages = []

    def on_msgServer(self, agent, *arg):
        # print('Received from %r: %s', agent, arg and str(arg) or '<no args>')
        # print('')
        # print(str(arg) or '<no args>')
        # print('')
        self.messages.append(arg)

    def on_msgPlayer(self, agent, *arg):
        # print('Received from %r: %s', agent, arg and str(arg) or '<no args>')
        # print('')
        # print(str(arg) or '<no args>')
        # print('')
        self.messages.append(arg)

    def initIvyGeneral(self, ip):
        IvyInit('IvyThread',
                'Started!',
                0,
                on_connection_change,
                on_die)

        '''TUTUT'''
        IvyStart(ip)
        # '127.0.0.1:2010'

    def bindIvyServer(self, bind):
        IvyBindMsg(self.on_msgServer, bind)
        # '(.*)'

        # print('Binded and ready!')

    def bindIvyPlayer(self, bind):
        IvyBindMsg(self.on_msgPlayer, bind)
        # '(.*)'

        # print('Binded and ready!')

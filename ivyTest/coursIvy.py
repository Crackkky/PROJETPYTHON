'''
Created on 3 Feb 2020

@author: crack
'''

from ivy.std_api import *

def on_connection_change(agent, event):
    if event == IvyApplicationDisconnected:
        print('Ivy application %r has disconnected', agent)
    else:
        print('Ivy application %r has connected', agent)
    print('Ivy applications currntly on the bus : %s', ','.join(IvyGetApplicationList()))


def on_die(agent, id):
    print('Received the order to die from %r with id = %d', agent, id)
    IvyStop()


# def on_msg(agent, *arg):
#    print('Received from %r: %s', agent, arg and str(arg) or '<no args>')

'''IvyInit('IvyScript', 
        'Hello!',
        0,
        on_connection_change,
        on_die
        )  
    
#TUTUT
IvyStart('127.0.0.1:2010')

msg = 'Hello there'
IvySendMsg(msg)

IvyBindMsg(on_msg, '(.*)')
    
print('Listening...')
#IvyStop()    '''

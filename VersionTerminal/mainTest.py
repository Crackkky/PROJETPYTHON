from ivy.std_api import *
from Projet.Model.IvyModel import *

ivyObject = IvyModel('127.0.0.1:2010')


def onmsgproc(*larg):
    print(larg)


IvyBindMsg(onmsgproc, '(.*)')
IvyGetApplicationList()
app = IvyGetApplication('IVYPROBE')
IvyGetApplicationName(app)
IvyGetApplicationHost(app)
IvySendDirectMsg(app, 765, 'glop')
IvySendDieMsg(app)

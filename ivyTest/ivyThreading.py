'''
Created on 3 Feb 2020

@author: crack
'''

import queue as Queue
from tkinter import *
import tkinter as tk
from ivyTest.coursIvy import *
from ivyTest.stuff import *


class TestClient(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        # Create the queue
        self.queue = Queue.Queue(100)
        self.running = 1
        
        # Set up the GUI part
        self.messageVar = stuffStringVar()

        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.grid()
        
        self.initIvy()
        
        # Start the periodic call in the GUI 
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        #Mettre les objets qui doivent etre modifie par Ivy dans la queue
        #puis modifier les objets ici

        if not self.queue.empty():
            currentMsg = self.queue.get()
            self.messageVar.run(currentMsg[0])
        
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(100, self.periodicCall)

    def endApplication(self):
        self.running = 0
        
    def send_message(self, msg):
        IvySendMsg(msg)
    
    def on_msg(self, agent, *arg):
        print('Received from %r: %s', agent, arg and str(arg) or '<no args>')
        self.queue.put(arg)
    
    def initIvy(self):
        IvyInit('IvyThread', 
        'Started!',
        0,
        on_connection_change,
        on_die)  
        
        '''TUTUT'''
        IvyStart('127.0.0.1:2010')
        IvyBindMsg(self.on_msg, '(.*)')
        
        
    def createWidgets(self):
        message_label = tk.Label(self, text = "Message receveid :")
        message_label.grid(row=0, column=0, sticky="nsew")
        
        message = tk.Label(self, textvariable = self.messageVar.strVar, borderwidth=2, relief="sunken")
        message.grid(row=0, column=1, sticky="nsew")
        
        entry_message = tk.Entry(self)
        entry_message.insert(10, "MessageToSend")
        entry_message.grid(row=2, column=0, sticky="nsew")
        
        send_button = tk.Button(self, text="send !",  command= lambda: self.send_message(entry_message.get()))
        send_button.grid(row=2, column=1, columnspan=2, sticky="nsew")


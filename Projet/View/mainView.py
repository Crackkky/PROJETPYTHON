'''
Created on 1 Feb 2020

@author: crack
'''

import tkinter as tk
from tkinter import *

from Projet.Model.lisa import *
from Projet.View.StyleInterface import buttonStyle, labelStyle


class MainView(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.buttonList = []
        self.label = None
        self.trainingButton = 0
        self.onlineButton = 1
        self.quitButton = 2
        self.createWidgets()
        self.grid()

    def createWidgets(self):

        positions = [(1, 1, 1), (1, 2, 1), (1, 3, 1)]
        self.label = tk.Label(self, borderwidth=2, relief="sunken")
        self.label.grid(row=0, column=1, columnspan=3)
        labelStyle(self.label)
        for pos in  positions:
            button = tk.Button(self)
            button.grid(row=pos[0], column=pos[1], columnspan=pos[2])
            self.buttonList.append(button)
            buttonStyle(button)

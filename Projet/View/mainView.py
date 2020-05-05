'''
Created on 1 Feb 2020

@author: crack
'''

import tkinter as tk
from tkinter import *

from Projet.Model.lisa import *


class MainView(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.buttonList = []
        self.trainingButton = 0
        self.serverButton = 1
        self.clientButton = 2
        self.quitButton = 3
        self.createWidgets()
        self.grid()

    def createWidgets(self):

        texts_button = ["Play in Training", "Play as Lisa (Server)", "Play as Jisoo (Client)", "Quit"]
        positions = [(1, 1, 1), (1, 2, 1), (1, 3, 1), (2, 1, 3)]

        label = tk.Label(self, text='Welcome to 블랙핑크 하우스!', borderwidth=2, relief="sunken")
        label.grid(row=0, column=1, columnspan=3)
        for text_button, pos in zip(texts_button, positions):
            button = tk.Button(self, text=text_button, borderwidth=1)
            button.grid(row=pos[0], column=pos[1], columnspan=pos[2])
            self.buttonList.append(button)

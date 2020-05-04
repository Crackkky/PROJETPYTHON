'''
Created on 1 Feb 2020

@author: crack
'''

from Projet.lisa import *
from tkinter import *
import tkinter as tk
from itertools import product



class MainInterface(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.grid()

    def createWidgets(self):
        texts_button = ["Play in Training", "Play as Lisa (Server)", "Quit"]
        fcts = [lambda:trainingMode(),lambda:serverMode(),lambda :sys.exit()]
        positions = [(1,1,1),(1,2,1),(2,1,2)]

        label = tk.Label(self, text='Welcome to 블랙핑크 하우스!', borderwidth=2, relief="sunken")
        label.grid(row=0, column=1, columnspan=2)
        for text_button, fct, pos in zip(texts_button, fcts, positions):
            button = tk.Button(self, text=text_button, borderwidth=1, command=fct)
            button.grid(row=pos[0], column=pos[1],columnspan=pos[2])








main = tk.Tk()

mainInterface = MainInterface(master = main)

mainInterface.mainloop()



import tkinter as tk

class TrainingView(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets(master)

    def createWidgets(self, master):
        master.geometry('500x500')
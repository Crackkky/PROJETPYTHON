import tkinter as tk

from Projet.View.trainingView import TrainingView


class TrainingController :
    def __init__(self):
        root = tk.Tk()
        self.trainingView = TrainingView(root)
        root.mainloop()
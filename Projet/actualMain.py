import tkinter as tk

from Projet.Controller.mainController import MainController
from Projet.Model.util import *

root= tk.Tk()
app = MainController(root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER)
root.mainloop()
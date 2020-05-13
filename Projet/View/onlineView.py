import tkinter as tk

from Projet.View.plateView import PlateView


class OnlineView(PlateView):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        super(OnlineView, self).__init__(checkPlateNumber, checkOperatorNumber, master)


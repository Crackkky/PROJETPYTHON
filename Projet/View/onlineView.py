import tkinter as tk

from Projet.View.plateView import PlateView
from Projet.View.styleInterface import frameStyle, labelStyle


class OnlineView(PlateView):
    def __init__(self, checkPlateNumber, checkOperatorNumber, master=None):
        super(OnlineView, self).__init__(checkPlateNumber, checkOperatorNumber, master)

        self.frameScore = tk.Frame(master)
        frameStyle(self.frameScore)
        self.scoreLabel = tk.Label(self.frameScore)
        labelStyle(self.scoreLabel)
        self.scoreLabel.pack(fill='both', expand=5)

        self.frameTime = tk.Frame(master)
        frameStyle(self.frameTime)
        self.timeLabel = tk.Label(self.frameTime)
        labelStyle(self.timeLabel)
        self.timeLabel.pack(fill='both', expand=5)

    def hideShowGame(self, show):
        super(OnlineView, self).hideShowGame(show)
        if show:
            self.frameScore.place(x=self.width - 70, y=0, width=70)
            self.frameTime.place(x=self.width - 80, y=self.height - 45, width=80)
        else:
            self.frameScore.place_forget()
            self.frameTime.place_forget()



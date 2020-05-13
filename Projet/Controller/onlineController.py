import tkinter as tk

from Projet.Controller.onlineClientController import OnlineClientController
from Projet.Controller.onlineServerController import OnlineServerController
from Projet.Controller.plateController import PlateController
from Projet.Model.onlineModel import OnlineModel
from Projet.View.plateView import PlateView


class OnlineController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER):
        super(OnlineController, self).__init__(parent, OnlineModel(),
                                               PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root), OPERATORS)

        self.view.hideShowGame(0)
        self.view.displayInfo("Looking for an opponent...")
        root.update()
        type = self.model.connect()
        root.destroy()
        root = tk.Tk()
        if type is self.model.SERVER:
            OnlineServerController(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, self.model.ivyObject)
        else :
            OnlineClientController(parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, self.model.ivyObject)
        root.mainloop()
import tkinter as tk

from Projet.Controller.onlineClientController import OnlineClientController
from Projet.Controller.onlineServerController import OnlineServerController
from Projet.Controller.plateController import PlateController
from Projet.Model.onlineModel import OnlineModel
from Projet.View.plateView import PlateView


class ConnectionMaker(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER):
        super(ConnectionMaker, self).__init__(parent, OnlineModel(),
                                               PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root), OPERATORS)
        self.parent = parent
        self.root = root
        self.plateNumber = PLATE_NUMBER
        self.view.hideShowGame(0)
        self.view.displayInfo("Looking for an opponent...")
        self.root.update()
        type = self.model.connect()
        self.root.destroy()
        self.root = tk.Tk()
        if type is self.model.SERVER:
            OnlineServerController(self.parent, self.root, self.operators, self.operatorNumber, self.plateNumber,
                                   self.model.ivyObject)
        else:
            OnlineClientController(self.parent, self.root, self.operators, self.operatorNumber, self.plateNumber,
                                   self.model.ivyObject)
        self.root.mainloop()
import tkinter as tk

from Projet.Controller.onlineClientController import OnlineClientController
from Projet.Controller.onlineServerController import OnlineServerController
from Projet.Controller.playableController import PlayableController
from Projet.Model.onlineModel import OnlineModel
from Projet.View.tileView import TileView


class ConnectionMaker(PlayableController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, TILE_NUMBER):
        super(ConnectionMaker, self).__init__(parent, OnlineModel(),
                                               TileView(TILE_NUMBER, OPERATOR_NUMBER, root), OPERATORS)
        self.parent = parent
        self.root = root
        self.maxTileNumber = TILE_NUMBER
        self.view.hideShowGame(0)
        self.view.displayInfo("Looking for an opponent...")
        self.root.update()
        self.model.connect(self.backMenu)
        self.root.destroy()
        self.root = tk.Tk()
        if self.model.isServer():
            OnlineServerController(self.parent, self.root, self.operators, self.operatorNumber, self.maxTileNumber, self.backMenu,
                                   self.model.ivyObject)
        else:
            OnlineClientController(self.parent, self.root, self.operators, self.operatorNumber, self.maxTileNumber, self.backMenu,
                                   self.model.ivyObject)
        self.root.mainloop()

    def backMenu(self, root=None):
        self.model.stopPlay()
        if root is None:
            super().backMenu(self.root)
        else:
            super().backMenu(root)
from Projet.Controller.tileController import TileController


class PlayableController(TileController):
    def __init__(self, parent, model, view, OPERATORS):
        super(PlayableController, self).__init__(parent, model, view, OPERATORS)

        self.completeButton("Validate", lambda: self.validate(), self.view.validateButton)

    def validate(self):

        if self.firstTile is not None and self.secondTile is not None and self.operator is not None:
            self.model.doPlay(self.firstTile, self.operators[self.operator], self.secondTile)
            # Suppresion de l'affichage de la dernière plaque
            self.view.showHideTileButton(self.model.lenSelectedTile, 0)
            if self.model.lenSelectedTile == 1:
                self.done()
            else:
                self.view.displayInfo()
            self.updateView()
        else:
            self.view.displayInfo("Please, select 2 tiles and 1 operator")

    def done(self):
        self.view.displayInfo("You got a difference of "
                              + str(self.model.getDifference())
                              + ", not Badr")
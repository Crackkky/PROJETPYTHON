from Projet.Controller.plateController import PlateController


class PlayableController(PlateController):
    def __init__(self, parent, model, view, OPERATORS):
        super(PlayableController, self).__init__(parent, model, view, OPERATORS)

        self.completeButton("Validate", lambda: self.validate(), self.view.validateButton)

    def validate(self):

        if self.firstPlate is not None and self.secondPlate is not None and self.operator is not None:
            self.model.doPlay(self.firstPlate, self.operators[self.operator], self.secondPlate)
            # Suppresion de l'affichage de la dernière plaque
            self.view.showHidePlateButton(self.model.lenSelectedPlate, 0)
            if self.model.lenSelectedPlate == 1:
                self.done()
            else:
                self.view.displayInfo()
            self.updateView()
        else:
            self.view.displayInfo("Please, select 2 plates and 1 operator")

    def done(self):
        self.view.displayInfo("You got a difference of "
                              + str(self.model.getDifference())
                              + ", not Badr")

    def updateView(self):
        super(PlayableController, self).updateView()
        self.view.historyLabel["text"] = "History" + self.model.historyToString()
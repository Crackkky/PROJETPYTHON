from Projet.Controller.plateController import PlateController
from Projet.Model.onlineModel import OnlineModel
from Projet.View.plateView import PlateView


class OnlineController(PlateController):
    def __init__(self, parent, root, OPERATORS, OPERATOR_NUMBER, PLATE_NUMBER, model = None, view = None):
        if view is None:
            view = PlateView(PLATE_NUMBER, OPERATOR_NUMBER, root)
        if model is None:
            model = OnlineModel()
        super(OnlineController, self).__init__(parent, model, view, OPERATORS)
        self.parent = parent
        self.root = root
        self.plateNumber = PLATE_NUMBER

    def found(self):
        self.model.found()
        self.view.displayInfo("Bravo")

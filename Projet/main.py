from random import *
from Projet.plate import *

print('Welcome in the training mode !')

goal = randint(100, 999)
possiblePlates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
#TODO en dur
selectedPlates = []

for i in range(1, 7):
    plateNumber = randint(0, 27) #TODO 27 en dur
    selectedPlates.append(plate(possiblePlates[plateNumber]))

selectedPlates = [plate(2), plate(4), plate(25), plate(1), plate(75), plate(9)]

printPlateArray(selectedPlates)

selectedPlates[1].operation(selectedPlates, 2)
printPlateArray(selectedPlates)











































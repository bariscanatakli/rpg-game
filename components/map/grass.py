arrayForGrass = list()
for array in range(24):
    arrayForGrass.append([i*0 for i in range(24)]) # grass implementing

from components.map.main import *

from components.map.drawObject import drawObject

grassIMG = pygame.image.load(currentDirectory+"\grass.png")


def drawGrass():
    drawObject(0, grassIMG, 0, 0, arrayForGrass, False)

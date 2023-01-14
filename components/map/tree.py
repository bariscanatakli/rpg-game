from components.map.main import *
from components.map.drawObject import drawObject

treeIMG = pygame.image.load(currentDirectory+"\Tree.png")
treeIMG = pygame.transform.scale(treeIMG, (128, 128))


def drawTree(arrays):
    drawObject(1, treeIMG, -64, -64, arrays, True)    


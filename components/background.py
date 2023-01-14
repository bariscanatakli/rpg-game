
from main import *
from components.map.main import *
from components.map.grass import drawGrass
from components.map.sand import drawSand
from components.map.water import drawWater
from components.map.tree import drawTree

# 0 means grass, #1 means tree
# s1 sandLeftTop, s2 sandTop s3 sandRightTop s4 sandLeft s5 sandMiddle s6 sandLeft s7 sandLeftDown s8 sDown s9 sandRightDown
currentDirectory = os.getcwd()+"\components\images"



def renderBackground(arrays, mapChanger):

    drawGrass()
    drawSand(arrays)
    drawWater(arrays)
    drawTree(arrays)
    # print(blockLists[mapChanger])
    pygame.image.save(window, currentDirectory+f"\Background{mapChanger}.png")

for map in maps:
    renderBackground(map, maps.index(map))

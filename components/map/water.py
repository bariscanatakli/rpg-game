from components.map.main import *
from components.map.drawObject import drawObject

currentDirectoryForSandsLeft = currentDirectory+"\water\waterLeft"
currentDirectoryForSandsMiddle = currentDirectory+"\water\waterMiddle"
currentDirectoryForSandsRight = currentDirectory+"\water\waterRight"

currentDirectoryForSandsCorner = currentDirectory+"\water\waterCorners"


# sand Left
waterLeftTop = pygame.image.load(
    currentDirectoryForSandsLeft+"\waterLeftTop.png")
waterLeft = pygame.image.load(currentDirectoryForSandsLeft+"\waterLeft.png")
waterLeftDown = pygame.image.load(
    currentDirectoryForSandsLeft+"\waterLeftDown.png")
# sand Mid
waterTop = pygame.image.load(currentDirectoryForSandsMiddle+"\waterTop.png")
waterMiddle = pygame.image.load(
    currentDirectoryForSandsMiddle+"\waterMiddle.png")
waterDown = pygame.image.load(
    currentDirectoryForSandsMiddle+"\waterDown.png")
# sand Right
waterRightTop = pygame.image.load(
    currentDirectoryForSandsRight+"\waterRightTop.png")
waterRight = pygame.image.load(
    currentDirectoryForSandsRight+"\waterRight.png")
waterRightDown = pygame.image.load(
    currentDirectoryForSandsRight+"\waterRightDown.png")
# sand corners
# sandLeftBottomOutside = pygame.image.load(
#     currentDirectoryForSandsCorner+"\sandLeftBottomOutside.png")
# sandLeftTopOutside = pygame.image.load(
#     currentDirectoryForSandsCorner+"\sandLeftTopOutside.png")
# sandRightBottomOutside = pygame.image.load(
#     currentDirectoryForSandsCorner+"\sandRightBottomOutside.png")
# sandRightTopOutside = pygame.image.load(
#     currentDirectoryForSandsCorner+"\sandRightTopOutside.png")
waterList = [waterLeftTop, waterTop, waterRightTop,
            waterLeft, waterMiddle, waterRight,
            waterLeftDown, waterDown, waterRightDown,
            ]
# sandList = [sandLeftTop, sandTop, sandRightTop,
#             sandLeft, sandMiddle, sandRight,
#             sandLeftDown, sandDown, sandRightDown,
#             sandLeftBottomOutside,
#             sandLeftTopOutside,
#             sandRightBottomOutside,
#             sandRightTopOutside
#             ]

def drawWater(arrays):
    for water in waterList:
        if water == waterLeftTop:
            drawObject("w1", waterLeftTop, 0, 0, arrays, False)
        elif water == waterLeft:
            drawObject("w4", waterLeft, 0, 0, arrays, False)
        elif water == waterLeftDown:
            drawObject("w7", waterLeftDown, 0, 0, arrays, False)
        elif water == waterTop:
            drawObject("w2", waterTop, 0, 0, arrays, False)
        elif water == waterMiddle:
            drawObject("w5", waterMiddle, 0, 0, arrays, False)
        elif water == waterDown:
            drawObject("w8", waterDown, 0, 0, arrays, False)
        elif water == waterRightTop:
            drawObject("w3", waterRightTop, 0, 0, arrays, False)
        elif water == waterRight:
            drawObject("w6", waterRight, 0, 0, arrays, False)
        elif water == waterRightDown:
            drawObject("w9", waterRightDown, 0, 0, arrays, False)
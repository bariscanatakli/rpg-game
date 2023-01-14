from components.map.main import *
from components.map.drawObject import drawObject

currentDirectoryForSandsLeft = currentDirectory+"\sand\sandLeft"
currentDirectoryForSandsMiddle = currentDirectory+"\sand\sandMiddle"
currentDirectoryForSandsRight = currentDirectory+"\sand\sandRight"
currentDirectoryForSandsCorner = currentDirectory+"\sand\sandCorners"


# sand Left
sandLeftTop = pygame.image.load(
    currentDirectoryForSandsLeft+"\sandLeftTop.png")
sandLeft = pygame.image.load(currentDirectoryForSandsLeft+"\sandLeft.png")
sandLeftDown = pygame.image.load(
    currentDirectoryForSandsLeft+"\sandLeftDown.png")
# sand Mid
sandTop = pygame.image.load(currentDirectoryForSandsMiddle+"\sandTop.png")
sandMiddle = pygame.image.load(
    currentDirectoryForSandsMiddle+"\sandMiddle.png")
sandDown = pygame.image.load(
    currentDirectoryForSandsMiddle+"\sandDown.png")
# sand Right
sandRightTop = pygame.image.load(
    currentDirectoryForSandsRight+"\sandRightTop.png")
sandRight = pygame.image.load(
    currentDirectoryForSandsRight+"\sandRight.png")
sandRightDown = pygame.image.load(
    currentDirectoryForSandsRight+"\sandRightDown.png")
# sand corners
sandLeftBottomOutside = pygame.image.load(
    currentDirectoryForSandsCorner+"\sandLeftBottomOutside.png")
sandLeftTopOutside = pygame.image.load(
    currentDirectoryForSandsCorner+"\sandLeftTopOutside.png")
sandRightBottomOutside = pygame.image.load(
    currentDirectoryForSandsCorner+"\sandRightBottomOutside.png")
sandRightTopOutside = pygame.image.load(
    currentDirectoryForSandsCorner+"\sandRightTopOutside.png")
sandList = [sandLeftTop, sandTop, sandRightTop,
            sandLeft, sandMiddle, sandRight,
            sandLeftDown, sandDown, sandRightDown,
            sandLeftBottomOutside,
            sandLeftTopOutside,
            sandRightBottomOutside,
            sandRightTopOutside
            ]

def drawSand(arrays):

    for sand in sandList:
        if sand == sandLeftTop:
            drawObject("s1", sandLeftTop, 0, 0, arrays, False)
        elif sand == sandLeft:
            drawObject("s4", sandLeft, 0, 0, arrays, False)
        elif sand == sandLeftDown:
            drawObject("s7", sandLeftDown, 0, 0, arrays, False)
        elif sand == sandTop:
            drawObject("s2", sandTop, 0, 0, arrays, False)
        elif sand == sandMiddle:
            drawObject("s5", sandMiddle, 0, 0, arrays, False)
        elif sand == sandDown:
            drawObject("s8", sandDown, 0, 0, arrays, False)
        elif sand == sandRightTop:
            drawObject("s3", sandRightTop, 0, 0, arrays, False)
        elif sand == sandRight:
            drawObject("s6", sandRight, 0, 0, arrays, False)
        elif sand == sandRightDown:
            drawObject("s9", sandRightDown, 0, 0, arrays, False)
        elif sand == sandLeftBottomOutside:
            drawObject("sLBO", sandLeftBottomOutside, 0, 0, arrays, False)
        elif sand == sandLeftTopOutside:
            drawObject("sLTO", sandLeftTopOutside, 0, 0, arrays, False)
        elif sand == sandRightBottomOutside:
            drawObject("sRBO", sandRightBottomOutside, 0, 0, arrays, False)
        elif sand == sandRightTopOutside:
            drawObject("sRTO", sandRightTopOutside, 0, 0, arrays, False)
from main import window, blockLists


def drawObject(id, imgName, xPos, yPos, array, blocked):
    blockPositions = list()
    xPosInitial = xPos
    for line in array:
        for i in line:
            if i == id:  
                window.blit(imgName, (xPos, yPos))
                if blocked:
                    blockPositions.append((xPos, yPos))

            xPos += 32
        yPos += 32
        xPos = xPosInitial
    if blocked:
        blockLists.append(blockPositions)


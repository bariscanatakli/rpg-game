
from main import *

currentDirectory = os.getcwd()+"\components\character\characterEffects"

class Energy:
    def __init__(self, scaleX, scaleY, xPos, yPos, velocity, moveRight, moveLeft, moveUp, moveDown, direction, shootIMG = pygame.image.load(currentDirectory+"\kaboom.png")) -> None:
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.xPos = xPos
        self.yPos = yPos
        self.velocity = velocity
        self.moveRight = moveRight
        self.moveUp = moveUp
        self.moveLeft = moveLeft
        self.moveDown = moveDown
        self.direction = direction
        self.shootIMG = shootIMG

    def shootShot(self):
        self.shootIMG = pygame.transform.scale(
            self.shootIMG, (self.scaleX, self.scaleY))

    def setDirection(self, direction):
        self.direction = direction

    def movementShot(self):

        if self.direction == "UP":
            self.yPos -= self.velocity*10
            # self.scaleY += self.velocity*2

        elif self.direction == "DOWN":
            self.yPos += self.velocity*10
            # self.scaleY += self.velocity*2

        elif self.direction == "LEFT":
            self.xPos -= self.velocity*10
            # self.scaleX += self.velocity*2

        elif self.direction == "RIGHT":
            self.xPos += self.velocity*10
            # self.scaleX += self.velocity*2

        # if self.scaleX>127 or self.scaleY>127:
            # self.scaleX, self.scaleY = 32,32

        

from main import *
from components.character.animation import *
from components.shot import *


class Character:
    def __init__(self, xPos=200, yPos=200, velocity=4, moveRight=False, moveLeft=False, moveUp=False, moveDown=False, name="unknown", direction="unknown", animationCounter=0, characterIMG=animationListFront[0], type="unknown", energy=Energy(32, 32, 9999, 9999, 2,
                                                                                                                                                                                                                                                 False, False, False, False, "")):
        self.xPos = xPos
        self.yPos = yPos
        self.velocity = velocity
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.name = name
        self.characterIMG = characterIMG
        self.direction = direction
        self.energy = energy
        self.animationCounter = animationCounter
        self.type = type

    def keyDown(self, event):
        self.animationCounter = 0
        if event.key == K_LEFT or event.key == K_a:
            self.moveRight = False
            self.moveLeft = True
            self.direction = "LEFT"

        if event.key == K_RIGHT or event.key == K_d:
            self.moveLeft = False
            self.moveRight = True
            self.direction = "RIGHT"

        if event.key == K_UP or event.key == K_w:
            self.moveDown = False
            self.moveUp = True
            self.direction = "UP"

        if event.key == K_DOWN or event.key == K_s:
            self.moveUp = False
            self.moveDown = True
            self.direction = "DOWN"

    def keyUp(self, event):
        if event.key == K_LEFT or event.key == K_a:
            self.moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            self.moveRight = False
        if event.key == K_UP or event.key == K_w:
            self.moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            self.moveDown = False

        if self.direction == "LEFT":
            self.characterIMG = pygame.image.load(
                currentDirectoryLeft+"\Left3.png")
        elif self.direction == "DOWN":
            self.characterIMG = pygame.image.load(
                currentDirectoryFront+"\Front3.png")
        elif self.direction == "UP":
            self.characterIMG = pygame.image.load(
                currentDirectoryInside+"\Inside3.png")
        elif self.direction == "RIGHT":
            self.characterIMG = pygame.image.load(
                currentDirectoryRight+"\Right3.png")

    def animationListSelector(self, direction):
        animationList = animationDict.get(direction)
        self.characterIMG = animationList[self.animationCounter]
        if self.animationCounter == len(animationList)-1:
            self.animationCounter = 0
        else:
            self.animationCounter += 1

    def movement(self):

        if self.moveDown:
            self.yPos += self.velocity
            self.animationListSelector("FRONT")
        if self.moveUp:
            self.yPos -= self.velocity
            self.animationListSelector("INSIDE")
        if self.moveLeft:
            self.xPos -= self.velocity
            self.animationListSelector("LEFT")
        if self.moveRight:
            self.xPos += self.velocity
            self.animationListSelector("RIGHT")

        return self.xPos, self.yPos

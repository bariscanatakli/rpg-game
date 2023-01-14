from main import *
from components.character.animation import *
from components.characterMovement import Character

# inheritence from Character


class Mob(Character):
    def __init__(self,xPos=100, yPos=100, velocity=1, moveRight=False, moveLeft=False, moveUp=False, moveDown=False, name="unknown", direction="unknown", animationCounter=0, characterIMG=animationListFront[0], type="unknown"):
        super().__init__(xPos, yPos, velocity, moveRight, moveLeft,
                         moveUp, moveDown, name, direction, animationCounter, characterIMG)

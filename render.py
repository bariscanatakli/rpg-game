from main import *
from components.background import *

from components.characterMovement import *
from components.mobMovement import *

user = Character()
deneme = Character()


mobs = {}
for mob in range(6):
    mobName = f"mob_{mob}"
    mobs.update({mobName: Mob(name = f"mob{mob}", type="mob", xPos=100*mob, yPos=100*mob)})

abilityList = list()

# mobs = {mob: mob.energy}
rendered = True
run = True


def findMovement(charPositions, treePos, user):
    for name, positions in charPositions.items():
        if positions[0] >= treePos["x1,x2"][0] and positions[0] <= treePos["x1,x2"][1]:
            if positions[1] >= treePos["y1,y3"][0] and positions[1] <= treePos["y1,y3"][1]:
                if user.moveLeft:
                    user.xPos += user.velocity
                    user.moveLeft = False
                if user.moveRight:
                    user.xPos -= user.velocity
                    user.moveRight = False
                if user.moveUp:
                    user.yPos += user.velocity
                    user.moveUp = False
                if user.moveDown:
                    user.yPos -= user.velocity
                    user.moveDown = False


while run:
    
    background = pygame.image.load(
        os.getcwd()+"\components\images"+f"/Background{mapChanger}.png")
    window.blit(background, (0, 0))
    
    for mobName, mob in mobs.items():
        # print(mob.xPos)
        if mob.xPos > user.xPos:
            mob.moveLeft = True
            mob.moveRight = False
            # print("mob sagda")
        if mob.xPos < user.xPos:
            mob.moveRight = True
            mob.moveLeft = False
            # print("mob solda")
        if mob.yPos < user.yPos:
            mob.moveDown = True
            mob.moveUp = False
            # print("mob yukarıda")
        if mob.yPos > user.yPos:
            mob.moveDown = False
            mob.moveUp = True
            # print("mob aşağıda")
       
        window.blit(mob.characterIMG, mob.movement())
    for event in pygame.event.get():
        # Closing the window and program if the
        # type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            user.keyDown(event)
            if event.key == pygame.K_SPACE:
                user.energy.xPos, user.energy.yPos = user.xPos, user.yPos
                user.energy.setDirection(user.direction)
                user.energy.shootShot()
        if event.type == pygame.KEYUP:
            user.keyUp(event)
        else:
            pass
    if user.yPos < -30:
        user.yPos = 700
        if mapChanger == len(maps) - 1:
            mapChanger = 0
        else:
            mapChanger += 1
    if user.yPos > 800:
        user.yPos = 0
        if mapChanger == 0:
            mapChanger = len(maps) - 1
        else:
            mapChanger -= 1
    if user.energy.shootIMG:
        user.energy.shootShot()
        user.energy.movementShot()
        window.blit(user.energy.shootIMG, (user.energy.xPos, user.energy.yPos))
    for everyPos in blockLists[mapChanger]:
        # print(user.xPos, user.yPos)
        treePos = {"x1,x2": (
            everyPos[0]+48, everyPos[0]+64), "y1,y3": (everyPos[1]+16, everyPos[1] + 64)}
        # print(everyPos, ":", everyPos[0]+24, everyPos[1]+56)
        charPositions = {"x1,y1": (user.xPos, user.yPos), "x2,y2": (
            user.xPos+24, user.yPos), "x3,y3": (user.xPos, user.yPos+56), "x4,y4": (user.xPos+24, user.yPos+56)}

        findMovement(charPositions, treePos, user)
    window.blit(user.characterIMG, user.movement())


    # Draws the surface object to the screen.
    pygame.display.update()
    clock.tick(60)

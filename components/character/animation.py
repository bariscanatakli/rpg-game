from main import *
currentDirectoryFront = os.getcwd()+"\components\character\Animations\Front"
currentDirectoryRight = os.getcwd()+"\components\character\Animations\Right"
currentDirectoryInside = os.getcwd()+"\components\character\Animations\Inside"
currentDirectoryLeft = os.getcwd()+"\components\character\Animations\Left"

animationListFront = list()
animationListRight = list()
animationListInside = list()
animationListLeft = list()

def animationListCreator(animationList,name, directory, tick):
    for animation in range(tick):
        animationList.append(pygame.image.load(directory+f"\{name}"))

animationListCreator(animationListFront,"Front1.png",currentDirectoryFront,9)
animationListCreator(animationListFront,"Front2.png",currentDirectoryFront,9)
# animationListCreator(animationListFront,"Front3.png",currentDirectoryFront,6)

animationListCreator(animationListRight,"Right1.png",currentDirectoryRight,6)
animationListCreator(animationListRight,"Right2.png",currentDirectoryRight,6)
animationListCreator(animationListRight,"Right3.png",currentDirectoryRight,6)

animationListCreator(animationListInside,"Inside1.png",currentDirectoryInside,9)
animationListCreator(animationListInside,"Inside2.png",currentDirectoryInside,9)
# animationListCreator(animationListInside,"Inside3.png",currentDirectoryInside,6)

animationListCreator(animationListLeft,"Left1.png",currentDirectoryLeft,6)
animationListCreator(animationListLeft,"Left2.png",currentDirectoryLeft,6)
animationListCreator(animationListLeft,"Left3.png",currentDirectoryLeft,6)

animationDict = {"FRONT": animationListFront,"RIGHT": animationListRight,"INSIDE": animationListInside,"LEFT": animationListLeft}


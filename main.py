# Importing pygame module
import pygame
from pygame.locals import *
import os
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
window = pygame.display.set_mode((768, 768))

blockLists = list()

clock = pygame.time.Clock()
# Add caption in the window
pygame.display.set_caption('caption')


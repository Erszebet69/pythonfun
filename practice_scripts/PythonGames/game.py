import pygame, sys
from pygame.locals import *

#initiate pygame, mandatory first line of script after imports
pygame.init()
#create game window
DISPLAYSURF = pygame.display.set_mode((400, 300))
#title of game window
pygame.display.set_caption("Hello World")
#creating reactangle object
spamRect = pygame.Rect(10, 20, 200, 300)
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #mandatory closing of pygame, must happen before sys exit
            sys.exit()
    #updates frame after event handling
    pygame.display.update()
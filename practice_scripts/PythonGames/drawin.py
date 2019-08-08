import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
#pygame.draw.polygon(surface, color, pointlist, width)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277),
(56, 277), (0, 106)))
#pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 40)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
#pygame.draw.lines(surface, color, closed, pointlist, width)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
#pygame.draw.circle(surface, color, center_point, radius, width)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
#pygame.draw.ellipse(surface, color, bounding_rectangle, width)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
#pygame.draw.rect(surface, color, rectangle_tuple, width)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

#set individual pixels with pixelArray object
#delete object when done drawing
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
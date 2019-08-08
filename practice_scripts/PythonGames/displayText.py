import pygame, sys
from pygame.locals import *
import time
"""
1. Create a pygame.font.Font object. (Like on line 12)
2. Create a Surface object with the text drawn on it by calling the Font object’s render()
method. (Line 13)
3. Create a Rect object from the Surface object by calling the Surface object’s
get_rect() method. (Line 14) This Rect object will have the width and height
correctly set for the text that was rendered, but the top and left attributes will be 0.
4. Set the position of the Rect object by changing one of its attributes. On line 15, we set the
center of the Rect object to be at 200, 150.
5. Blit the Surface object with the text onto the Surface object returned by
pygame.display.set_mode(). (Line 19)
6. Call pygame.display.update() to make the display Surface appear on the screen.
(Line 24)
"""


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

pygame.mixer.music.load('robot.wav')
pygame.mixer.music.play(-1, 0.0)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
#The parameters to the pygame.font.Font() constructor function is a string of the font file to use and an integer of the size of the font
fontObj = pygame.font.Font('freesansbold.ttf', 32)
#the Render method will draw the text on the surface
#The parameters to the render() method call are a string of the text to render, a Boolean value to specify if we want anti-aliasing, the color of the text, and the color of the background.
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

#play sound


while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
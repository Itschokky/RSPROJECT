import pygame
from Setting import *
from Level import *
pygame.init()



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test")
bg = pygame.image.load('img/Background/forest.png')
#setframe rate
clock = pygame.time.Clock()
FPS = 60
level = Level(level_map, screen)

#player action variables
moving_left = False
moving_right = False

BG = (0, 0, 0)

def draw_bg():
    screen.fill('black')



run = True
while run:

    clock.tick(FPS)

    draw_bg()

    level.run()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
import pygame
from spritesheet import SpriteSheet
from consts import *

pygame.init()

dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyGame test')

clock = pygame.time.Clock()

# spritesheet do galo
ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())

run = True
while run:
    dis.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

import pygame
from spritesheet import SpriteSheet
from galo import Galo
from consts import *

pygame.init()

dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyGame test')

clock = pygame.time.Clock()

# spritesheet do galo
ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
galo = Galo(450, 350, 3, ss, 4, 10)  # criando um galo

run = True
while run:
    dis.fill((50, 50, 50))
    galo.tick()
    galo.render(dis)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                galo.setStatus(STT_WALKING)
                galo.setDir(DIR_RIGTH)
            if event.key == pygame.K_a:
                galo.setStatus(STT_WALKING)
                galo.setDir(DIR_LEFT)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                galo.setStatus(STT_STOPED)
            if event.key == pygame.K_a:
                galo.setStatus(STT_STOPED)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

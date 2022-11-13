import pygame
from spritesheet import SpriteSheet
from galo import Galo
from world import World
from colision_box import Colision_box
from consts import *

pygame.init()

dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyGame test')

clock = pygame.time.Clock()

# spritesheet do galo
ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
galo = Galo(450, 350, ENTITIES_SIZE, ENTITIES_SIZE, 3, ss, 4, 10, Colision_box(450, 350, 30, 30, 4 * SCALE, 8 * SCALE))
mundo = World()

run = True
while run:
    dis.fill((50, 50, 50))
    galo.tick(mundo)
    mundo.render(dis)
    galo.render(dis)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_d:
                galo.setStatus(STT_WALKING)
                galo.setDir(DIR_RIGTH)
            if event.key == pygame.K_a:
                galo.setStatus(STT_WALKING)
                galo.setDir(DIR_LEFT)
            if event.key == pygame.K_w:
                if galo.colidiuY(mundo):
                    galo.jumping = True
                    galo.gravity = GRAVITY_JUMP
                elif galo.jumping:
                    galo.jumping = False
                    galo.gravity = GRAVITY_SJUMP

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if galo.dir == DIR_RIGTH:
                    galo.setStatus(STT_STOPED)
            if event.key == pygame.K_a:
                if galo.dir == DIR_LEFT:
                    galo.setStatus(STT_STOPED)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

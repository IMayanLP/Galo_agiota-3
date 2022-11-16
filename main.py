import pygame

from game import Game
from consts import *

pygame.init()

pygame.font.init()
pygame.font.get_init()

dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Galo Agiota 3')

font = pygame.font.SysFont('fonts/Minecrafter.Reg.ttf', 50)

clock = pygame.time.Clock()

game = Game()
while game.checkIsRunning():
    dis.fill((50, 50, 50))
    game.tick()
    game.render(dis, font)
    game.events()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

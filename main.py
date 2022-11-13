import pygame
from game import Game
from consts import *

pygame.init()

dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyGame test')

clock = pygame.time.Clock()

game = Game()
while game.checkIsRunning():
    dis.fill((50, 50, 50))
    game.tick()
    game.render(dis)
    game.events()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

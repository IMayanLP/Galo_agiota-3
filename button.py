import pygame
from consts import *


class Button:
    def __init__(self, x, y, image):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * SCALE), int(height * SCALE)))
        self.colisionBox = self.image.get_rect()
        self.colisionBox.topleft = (x, y)

    def render(self, dis):
        dis.blit(self.image, (self.colisionBox.x, self.colisionBox.y))

    def click(self, x, y):
        if self.colisionBox.collidepoint(x, y):
            return True
        return False

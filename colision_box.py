import pygame
from consts import *

class Colision_box():
    def __init__(self, x, y, width, height, distance_x, distance_y):
        self.x = x
        self.y = y
        self.w = width * SCALE
        self.h = height * SCALE
        self.distance_y = distance_y
        self.distance_x = distance_x

    def update(self, newX, newY):
        self.x = newX + self.distance_x
        self.y = newY + self.distance_y

    def render(self, display):
        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(self.x, self.y, self.w, self.h), 1)
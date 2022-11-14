import pygame
from consts import *

class Camera:
    def __init__(self, start, end, vel):
        self.displacement = start
        self.start = start
        self.end = end
        self.vel = vel
        self.moving = True

    def tick(self):
        if self.displacement + SCREEN_WIDTH < self.end:
            self.displacement += self.vel
        else:
            self.moving = False

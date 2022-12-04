import pygame
from consts import *


class Sky:
    def __init__(self, image, vel):
        width = image.get_width()
        height = image.get_height()
        self.image1 = pygame.transform.scale(image, (int(width * SCALE), int(height * SCALE)))
        self.image2 = pygame.transform.flip(self.image1, True, False)
        self.w = self.image1.get_width()
        self.h = self.image1.get_height()
        self.x1 = 0
        self.x2 = self.x1 + self.w
        self.y = 0
        self.vel = vel
        self.moving = True

    def tick(self, camera):
        if not camera.moving:
            self.moving = False
        if self.moving:
            if self.x1 + self.w < -10:
                self.x1 = self.x2 + self.w
            if self.x2 + self.w < -10:
                self.x2 = self.x1 + self.w
            self.x1 -= self.vel
            self.x2 -= self.vel

    def render(self, dis):
        dis.blit(self.image1, (self.x1, self.y))
        dis.blit(self.image2, (self.x2, self.y))

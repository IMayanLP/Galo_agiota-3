from random import random
from entity import Entity
from consts import *

class Slime(Entity):
    gravity = 0
    dead = False
    range = 150
    timer = 0

    def setGravity(self, newGravity):
        self.gravity = newGravity

    def tick(self, world, galo):
        if not self.dead:
            self.colisionBox.update(self.x, self.y)
            distance = galo.x - self.x
            if distance < 0: distance *= -1
            if distance < self.range:
                if galo.x < self.x:
                    self.dir = DIR_LEFT
                else:
                    self.dir = DIR_RIGTH
            else:
                if int(random() * 1000) % 17 == 0:
                    self.dir *= -1

            if not self.collisionY(world):
                self.gravity += 1
                self.y += self.gravity
            else:
                self.gravity = 0

            if not self.collisionX(world):
                if self.x + self.vel * self.dir < 1200:
                    self.x += self.vel * self.dir
            else:
                if self.collisionY(world):
                    self.gravity = -15
        else:
            self.timer += 1
            self.y += 10

        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += 0.2

    def render(self, display, camera):
        if not self.dead:
            display.blit(self.ss[0][int(self.frame)], (self.x - camera.displacement, self.y))
        else:
            display.blit(self.ss[1][int(self.frame)], (self.x - camera.displacement, self.y))

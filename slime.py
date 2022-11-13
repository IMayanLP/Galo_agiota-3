from random import random
from entity import Entity
from consts import *

class Slime(Entity):
    gravity = 0
    range = 150
    deadTimer = 0

    def setGravity(self, newGravity):
        self.gravity = newGravity

    def tick(self, world, galo):
        if self.alive:
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
                self.setGravity(self.gravity + 1)
                self.y += self.gravity
            else:
                self.setGravity(NO_GRAVITY)

            if not self.collisionX(world):
                if self.x + (self.vel * self.dir) < world.width * SPRITE_SIZE * SCALE:
                    self.x += self.vel * self.dir
            else:
                if self.collisionY(world):
                    self.setGravity(GRAVITY_SJUMP)
        else:
            self.deadTimer += 1
            self.y += 10

        self.animate()

    def render(self, display, camera):
        if self.alive:
            display.blit(self.ss[0][int(self.frame)], (self.x - camera.displacement, self.y))
        else:
            display.blit(self.ss[1][int(self.frame)], (self.x - camera.displacement, self.y))

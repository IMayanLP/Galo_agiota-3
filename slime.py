from random import random
from entity import Entity
from consts import *


class Slime(Entity):
    gravity = 0
    range = 150
    deadTimer = 0
    damage = 1

    def setGravity(self, newGravity):
        self.gravity = newGravity

    def tick(self, world, galo):
        self.colisionBox.update(self.x, self.y)
        if self.alive:
            distance = self.set_distance(galo)
            if distance < self.range:
                if galo.x < self.x:
                    self.dir = DIR_LEFT
                else:
                    self.dir = DIR_RIGTH
            else:
                if self.swap_dir(world):
                    self.dir *= -1
                if int(random() * 1000) % 17 == 0:
                    self.dir *= -1

            if not self.collisionY(world):
                self.setGravity(self.gravity + 1)
                self.y += self.gravity
            else:
                self.setGravity(NO_GRAVITY)

            if not self.collisionX(world):
                if self.status == STT_WALKING:
                    if self.x + (self.vel * self.dir) < world.width * SPRITE_SIZE * SCALE:
                        self.x += self.vel * self.dir
            else:
                if self.collisionY(world):
                    self.setGravity(GRAVITY_SJUMP)
        else:
            self.deadTimer += 1
            if not self.collisionY(world):
                self.setGravity(self.gravity + 1)
                self.y += self.gravity
            else:
                self.setGravity(NO_GRAVITY)

        self.animate()

    def render(self, display, camera):
        if self.alive:
            display.blit(self.ss[0][int(self.frame)], (self.x - camera.displacement, self.y))
        else:
            display.blit(self.ss[1][int(self.frame)], (self.x - camera.displacement, self.y))

    def swap_dir(self, world):
        x0 = self.coordToMatriz(self.colisionBox.x + (self.vel * self.dir))
        y = self.coordToMatriz(self.colisionBox.y + self.colisionBox.h + self.gravity)
        x1 = self.coordToMatriz(self.colisionBox.x + self.colisionBox.w + (self.vel * self.dir))
        if y > world.heigth - 1:
            return False
        if x1 > world.width - 1:
            return True
        for i in range(y, world.heigth):
            if world.blocks[x0][i] is not None or world.blocks[x1][i] is not None:
                return False
        return True

    def set_distance(self, galo):
        x = galo.x - self.x
        if x < 0:
            return -x
        return x

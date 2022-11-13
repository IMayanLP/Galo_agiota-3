import pygame
from entity import Entity
from world import World
from consts import *


class Galo(Entity):
    gravity = 0

    def setStatus(self, newStatus):
        self.status = newStatus
        self.frame = 0

    def setDir(self, newDir):
        self.dir = newDir

    def setGravity(self, newGravity):
        self.gravity = newGravity

    def coordToMatriz(self, coord):
        return int(coord / (SPRITE_SIZE * SCALE))

    def tick(self, world):
        if self.status == STT_WALKING:
            if not self.colidiuX(world):
                self.x += self.vel * self.dir

        if not self.colidiuY(world):
            self.gravity += 1
            self.y += self.gravity
        else:
            self.gravity = 0

        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += 0.2

    def render(self, display):
        if self.status == STT_WALKING:
            if self.dir == DIR_RIGTH: display.blit(self.ss[0][int(self.frame)], (self.x, self.y))
            else: display.blit(self.ss[1][int(self.frame)], (self.x, self.y))

        elif self.status == STT_STOPED:
            if self.dir == DIR_RIGTH: display.blit(self.ss[2][int(self.frame)], (self.x, self.y))
            else: display.blit(self.ss[3][int(self.frame)], (self.x, self.y))

    def colidiuY(self, world):
        x0 = self.coordToMatriz(self.x)
        y1 = self.coordToMatriz(self.y + (self.h * SCALE) + self.gravity)
        x1 = self.coordToMatriz(self.x + (self.w * SCALE))
        y0 = self.coordToMatriz(self.y + self.gravity + 15)
        if world.blocks[x0][y1] is not None:
            if world.blocks[x0][y1].type == 1:
                return True
        if world.blocks[x1][y1] is not None:
            if world.blocks[x1][y1].type == 1:
                return True
        if world.blocks[x0][y0] is not None:
            if world.blocks[x0][y0].type == 1:
                return True
        if world.blocks[x1][y0] is not None:
            if world.blocks[x1][y0].type == 1:
                return True
        return False

    def colidiuX(self, world):
        x0 = self.coordToMatriz(self.x + (self.w * SCALE) + (self.vel * self.dir))
        x1 = self.coordToMatriz(self.x + (self.vel * self.dir))
        y0 = self.coordToMatriz(self.y - 1)
        y1 = self.coordToMatriz(self.y + (self.h * SCALE) - 1)
        if world.blocks[x0][y1] is not None:
            if world.blocks[x0][y1].type == 1:
                return True
        if world.blocks[x0][y0] is not None:
            if world.blocks[x0][y0].type == 1:
                return True
        if world.blocks[x1][y0] is not None:
            if world.blocks[x1][y0].type == 1:
                return True
        if world.blocks[x1][y1] is not None:
            if world.blocks[x1][y1].type == 1:
                return True
        return False
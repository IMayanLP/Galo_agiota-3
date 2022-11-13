import pygame
from entity import Entity
from colision_box import Colision_box
from consts import *


class Galo(Entity):
    gravity = 0
    jumping = False

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
        self.colisionBox.update(self.x, self.y)
        if self.status == STT_WALKING:
            if not self.colidiuX(world):
                self.x += self.vel * self.dir

        if not self.colidiuY(world):
            self.gravity += 1
            self.y += self.gravity
        else:
            self.jumping = False
            self.gravity = 0

        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += 0.2

    def render(self, display):
        self.colisionBox.render(display)
        if self.status == STT_WALKING:
            if self.dir == DIR_RIGTH: display.blit(self.ss[0][int(self.frame)], (self.x, self.y))
            else: display.blit(self.ss[1][int(self.frame)], (self.x, self.y))

        elif self.status == STT_STOPED:
            if self.dir == DIR_RIGTH: display.blit(self.ss[2][int(self.frame)], (self.x, self.y))
            else: display.blit(self.ss[3][int(self.frame)], (self.x, self.y))

    def colidiuY(self, world):
        x0 = self.coordToMatriz(self.colisionBox.x)
        y1 = self.coordToMatriz(self.colisionBox.y + self.colisionBox.h + self.gravity)
        x1 = self.coordToMatriz(self.colisionBox.x + self.colisionBox.w)
        y0 = self.coordToMatriz(self.colisionBox.y + self.gravity + 15)
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
        x0 = self.coordToMatriz(self.colisionBox.x + self.colisionBox.w + (self.vel * self.dir))
        x1 = self.coordToMatriz(self.colisionBox.x + (self.vel * self.dir))
        y0 = self.coordToMatriz(self.colisionBox.y - 1)
        y1 = self.coordToMatriz(self.colisionBox.y + self.colisionBox.h - 1)
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
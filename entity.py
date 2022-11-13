from abc import ABC, abstractmethod
from consts import *


class Entity(ABC):
    def __init__(self, x, y, w, h, vel, status, spritesheet, maxLines, maxframes, colisionBox):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colisionBox = colisionBox
        self.status = status
        self.vel = vel
        self.dir = DIR_RIGTH
        self.status = 0
        self.frame = 0
        self.ss = []
        for i in range(maxLines):
            sprites = []
            for j in range(maxframes):
                sprites.append(spritesheet.get_image(j, i, w, h, SCALE, (0, 0, 0)))
            self.ss.append(sprites)

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, display):
        pass

    def collisionY(self, world):
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

    def collisionX(self, world):
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

    def coordToMatriz(self, coord):
        return int(coord/(SPRITE_SIZE*SCALE))
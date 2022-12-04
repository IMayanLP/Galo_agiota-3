from abc import ABC, abstractmethod
from consts import *


def is_Colliding(p0, p1, x0, x1, y0, y1):
    if x0 <= p0 <= x1 and y0 <= p1 <= y1:
        return True
    return False


def check_Block_Collision(world, x0, x1, y0, y1):
    if x0 not in range(0, world.width)\
            or x1 not in range(0, world.width)\
            or y0 not in range(0, world.heigth)\
            or y1 not in range(0, world.heigth):
        return True
    if world.blocks[x0][y1] is not None:
        if world.blocks[x0][y1].ColisionType:
            return True
    if world.blocks[x0][y0] is not None:
        if world.blocks[x0][y0].ColisionType:
            return True
    if world.blocks[x1][y0] is not None:
        if world.blocks[x1][y0].ColisionType:
            return True
    if world.blocks[x1][y1] is not None:
        if world.blocks[x1][y1].ColisionType:
            return True
    return False


class Entity(ABC):
    def __init__(self, x, y, w, h, vel, status, spritesheet, maxLines, maxframes, colisionBox, e_scale):
        self.alive = True
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colisionBox = colisionBox
        self.status = status
        self.vel = vel
        self.dir = DIR_RIGTH
        self.frame = 0
        self.ss = []
        for i in range(maxLines):
            sprites = []
            for j in range(maxframes):
                sprites.append(spritesheet.get_image(j, i, w, h, e_scale, (0, 0, 0)))
            self.ss.append(sprites)

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, display):
        pass

    def animate(self):
        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += ANIMATION_SPEED

    def collisionY(self, world):
        x0 = self.coordToMatriz(self.colisionBox.x)
        y1 = self.coordToMatriz(self.colisionBox.y + self.colisionBox.h + self.gravity)
        x1 = self.coordToMatriz(self.colisionBox.x + self.colisionBox.w)
        y0 = self.coordToMatriz(self.colisionBox.y + self.gravity + 15)
        if y1 > world.heigth - 1:
            self.alive = False
            return True
        if check_Block_Collision(world, x0, x1, y0, y1):
            return True
        return False

    def collisionX(self, world):
        x0 = self.coordToMatriz(self.colisionBox.x + self.colisionBox.w + (self.vel * self.dir))
        x1 = self.coordToMatriz(self.colisionBox.x + (self.vel * self.dir))
        y1 = self.coordToMatriz(self.colisionBox.y + self.colisionBox.h - 1)
        y0 = self.coordToMatriz(self.colisionBox.y - 1)
        if x0 > world.width - 1:
            return True
        if check_Block_Collision(world, x0, x1, y0, y1):
            return True
        return False

    def check_Collision(self, e2):
        x0 = self.colisionBox.x
        x1 = self.colisionBox.x + self.colisionBox.w
        y0 = self.colisionBox.y
        y1 = self.colisionBox.y + self.colisionBox.h
        if is_Colliding(x0, y1, e2.colisionBox.x, e2.colisionBox.x + e2.colisionBox.w, e2.y, e2.colisionBox.y + e2.colisionBox.h) \
                or is_Colliding(x1, y1, e2.colisionBox.x, e2.colisionBox.x + e2.colisionBox.w, e2.colisionBox.y, e2.colisionBox.y + e2.colisionBox.h) \
                or is_Colliding(x0, y0, e2.colisionBox.x, e2.colisionBox.x + e2.colisionBox.w, e2.colisionBox.y, e2.colisionBox.y + e2.colisionBox.h) \
                or is_Colliding(x1, y0, e2.colisionBox.x, e2.colisionBox.x + e2.colisionBox.w, e2.colisionBox.y, e2.colisionBox.y + e2.colisionBox.h):
            return True
        return False

    def coordToMatriz(self, coord):
        return int(coord / (SPRITE_SIZE * SCALE))

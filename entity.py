from abc import ABC, abstractmethod
from consts import *


class Entity(ABC):
    def __init__(self, x, y, vel, spritesheet, maxLines, maxframes):
        self.x = x
        self.y = y
        self.vel = vel
        self.dir = DIR_RIGTH
        self.status = 0
        self.frame = 0
        self.ss = []
        for i in range(maxLines):
            sprites = []
            for j in range(maxframes):
                sprites.append(spritesheet.get_image(j, i, 38, 38, 2, (0, 0, 0)))
            self.ss.append(sprites)

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, display):
        pass

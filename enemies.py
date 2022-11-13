from slime import Slime
from colision_box import Colision_box
from consts import *


class Enemies:
    def __init__(self, slimes_amount, sprites):
        self.enemies = {'slimes': []}
        self.sprites = sprites
        self.spawn = 0
        for i in range(slimes_amount):
            self.enemies['slimes'].append(Slime(i*300, 0, 38, 38, 2, STT_WALKING, sprites, 2, 10, Colision_box(i*300, 0, 30, 30, 4 * SCALE, 8 * SCALE)))

    def tick(self, world, galo):
        if self.spawn >= 300:
            self.enemies['slimes'].append(Slime(galo.x + 150, 0, 38, 38, 2, STT_WALKING, self.sprites, 2, 10, Colision_box(galo.x + 150, 0, 30, 30, 4 * SCALE, 8 * SCALE)))
            self.spawn = 0
        else:
            self.spawn += 1

        for i in range(len(self.enemies['slimes'])):
            if self.enemies['slimes'][i] is not None:
                if self.enemies['slimes'][i].timer > 50:
                    self.enemies['slimes'][i] = None
                else:
                    self.enemies['slimes'][i].tick(world, galo)

    def render(self, display, camera):
        for i in range(len(self.enemies['slimes'])):
            if self.enemies['slimes'][i] is not None:
                self.enemies['slimes'][i].render(display, camera)

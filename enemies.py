from slime import Slime
from colision_box import Colision_box
from consts import *


class Enemies:
    def __init__(self, slimes_amount, sprites):
        self.enemies = {'slimes': []}
        for i in range(slimes_amount):
            self.enemies['slimes'].append(Slime(i*300, 350, 38, 38, 2, STT_WALKING, sprites, 2, 10, Colision_box(i*300, 350, 30, 30, 4 * SCALE, 8 * SCALE)))

    def tick(self, world, galo):
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

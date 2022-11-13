from consts import *

class Block():
    def __init__(self, sprite, x, y, type):
        self.sprite = sprite.get_image(0, 0, SPRITE_SIZE, SPRITE_SIZE, SCALE, (0, 0, 0))
        self.type = type
        self.x = x
        self.y = y
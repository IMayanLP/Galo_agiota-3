from consts import *

class Block():
    def __init__(self, sprite, x, y, ColisionType):
        self.sprite = sprite.get_image(0, 0, SPRITE_SIZE, SPRITE_SIZE, SCALE, (0, 0, 0))
        self.ColisionType = ColisionType
        self.x = x
        self.y = y
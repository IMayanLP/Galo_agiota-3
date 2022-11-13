import pygame
from block import Block
from spritesheet import SpriteSheet
from consts import *

class World:
    def __init__(self):
        self.phase = 0
        self.name = "fase" + str(self.phase) + ".txt"
        self.blocks = []
        self.entities = []
        sps = SpriteSheet(pygame.image.load('src/grama.png').convert_alpha())
        for i in range(20):
            line = []
            for j in range(12):
                if j >= 10: line.append(Block(sps, i*SPRITE_SIZE, j*SPRITE_SIZE, 1))
                else: line.append(None)
            self.blocks.append(line)
        self.blocks[7][7] = Block(sps, 7*SPRITE_SIZE, 7*SPRITE_SIZE, 1)
        self.blocks[10][9] = Block(sps, 10 * SPRITE_SIZE, 9 * SPRITE_SIZE, 1)
        self.blocks[5][8] = Block(sps, 5 * SPRITE_SIZE, 8 * SPRITE_SIZE, 1)

    def render(self, display):
        for i in range(20):
            pygame.draw.line(display, (255, 0, 255), (i * SCALE * SPRITE_SIZE, 0), (i * SCALE * SPRITE_SIZE, SCREEN_HEIGHT))
            for j in range(12):
                pygame.draw.line(display, (0, 0, 255), (0, j * SCALE * SPRITE_SIZE), (SCREEN_WIDTH, j * SCALE * SPRITE_SIZE))
                if self.blocks[i][j] is not None:
                    display.blit(self.blocks[i][j].sprite, (self.blocks[i][j].x * SCALE, self.blocks[i][j].y * SCALE))
import pygame
import json
from block import Block
from spritesheet import SpriteSheet
from consts import *

class World:
    def __init__(self, w, h):
        self.phase = 1
        self.name = "fase" + str(self.phase) + ".txt"
        self.blocks = []
        self.entities = []
        self.width = w
        self.height = h
        sps = SpriteSheet(pygame.image.load('src/grama.png').convert_alpha())
        for i in range(w):
            line = []
            for j in range(h):
                line.append(None)
            self.blocks.append(line)

        with open('maps/map1.json', 'r') as map:
            decode = json.load(map)

        for obj in decode["blocos"]:
            self.blocks[obj["j"]][obj["i"]] = Block(sps, obj["j"] * SPRITE_SIZE, obj["i"] * SPRITE_SIZE, 1)

        self.width = len(self.blocks)
        self.heigth = len(self.blocks[0])

    def render(self, display, camera):
        for i in range(self.width):
            pygame.draw.line(display, (255, 0, 255), (i * SCALE * SPRITE_SIZE - camera.displacement, 0), (i * SCALE * SPRITE_SIZE - camera.displacement, SCREEN_HEIGHT))
            for j in range(self.heigth):
                pygame.draw.line(display, (0, 0, 255), (0, j * SCALE * SPRITE_SIZE), (SCREEN_WIDTH, j * SCALE * SPRITE_SIZE))
                if self.blocks[i][j] is not None:
                    display.blit(self.blocks[i][j].sprite, (self.blocks[i][j].x * SCALE - camera.displacement, self.blocks[i][j].y * SCALE))
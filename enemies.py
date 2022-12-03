import pygame

from coin import Coin
from slime import Slime
from colision_box import Colision_box
from consts import *


def set_spawn_x(galo, world):
    x = galo.colisionBox.x + galo.colisionBox.w + 150
    if galo.coordToMatriz(x) >= world.width - 1:
        x = galo.x - 300
    return x


class Enemies:
    def __init__(self, slimes_amount, sprites, spawn_counter):
        self.coin_song = pygame.mixer.Sound('sounds/coin.mp3')
        self.coin_song.set_volume(0.2)
        self.enemies = {'slimes': [],
                        'coins': []}
        self.sprites = sprites
        self.spawn_counter = spawn_counter
        self.spawn = 0
        for i in range(slimes_amount):
            self.enemies['slimes'].append(Slime(i*300, 0, ENTITIES_SIZE, ENTITIES_SIZE, 2, STT_WALKING, sprites[0], 2, 10, Colision_box(i*300, 0, 30, 30, 4 * SCALE, 8 * SCALE), SCALE))

    def tick(self, world, galo):
        if self.spawn >= self.spawn_counter:
            x = set_spawn_x(galo, world)
            self.enemies['slimes'].append(Slime(x, 0, ENTITIES_SIZE, ENTITIES_SIZE, 2, STT_WALKING, self.sprites[0], 2, 10, Colision_box(galo.x + 150, 0, 30, 30, 4 * SCALE, 8 * SCALE), SCALE))
            self.spawn = 0
        else:
            self.spawn += 1

        for i in range(len(self.enemies['slimes'])):
            if self.enemies['slimes'][i] is not None:
                if self.enemies['slimes'][i].deadTimer > 50:
                    self.enemies['coins'].append(Coin(self.enemies['slimes'][i].x, self.enemies['slimes'][i].y, ENTITIES_SIZE, ENTITIES_SIZE, 0, STT_STOPED, self.sprites[1], 1, 8, Colision_box(self.enemies['slimes'][i].x, self.enemies['slimes'][i].y, ENTITIES_SIZE / 2, ENTITIES_SIZE / 2, 0, 0), 1))
                    self.enemies['slimes'][i] = None
                else:
                    self.enemies['slimes'][i].tick(world, galo)

        for i in range(len(self.enemies['coins'])):
            if self.enemies['coins'][i] is not None:
                self.enemies['coins'][i].tick(galo)
                if self.enemies['coins'][i].caught:
                    galo.score += 1
                    self.coin_song.play()
                    self.enemies['coins'][i] = None

    def render(self, display, camera):
        for i in range(len(self.enemies['slimes'])):
            if self.enemies['slimes'][i] is not None:
                self.enemies['slimes'][i].render(display, camera)
        for i in range(len(self.enemies['coins'])):
            if self.enemies['coins'][i] is not None:
                self.enemies['coins'][i].render(display, camera)

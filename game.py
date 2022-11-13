import pygame
from random import random
from consts import *
from galo import Galo
from camera import Camera
from enemies import Enemies
from world import World
from colision_box import Colision_box
from spritesheet import SpriteSheet

class Game:
    def __init__(self):
        # spritesheets
        galo_ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
        slime_ss = SpriteSheet(pygame.image.load('src/spritesslime.png').convert_alpha())
        heart_ss = SpriteSheet(pygame.image.load('src/hearts.png').convert_alpha())
        grama_ss = SpriteSheet(pygame.image.load('src/grama.png').convert_alpha())
        self.stage = 0
        self.interface = {
            'heartSprite': []
        }
        for i in range(2):
            self.interface['heartSprite'].append(heart_ss.get_image(i, 0, SPRITE_SIZE, SPRITE_SIZE, 1, (0, 0, 0)))
        self.galo = Galo(350, 350, ENTITIES_SIZE, ENTITIES_SIZE, 3, STT_STOPED, galo_ss, 4, 10, Colision_box(350, 350, 30, 30, 4 * SCALE, 8 * SCALE))
        self.mundo = World(101, 11, grama_ss, 'map1.json')
        self.cam = Camera(0, self.mundo.width * SPRITE_SIZE * SCALE, 2)
        self.inimigos = Enemies(int(random()*10), slime_ss)
        self.run = True

    def tick(self):
        if self.galo.currentLife <= 0:
            self.run = False
        self.cam.tick()
        self.inimigos.tick(self.mundo, self.galo)
        self.galo.tick(self.mundo, self.inimigos)

    def render(self, dis):
        self.mundo.render(dis, self.cam)
        self.inimigos.render(dis, self.cam)
        self.galo.render(dis, self.cam)
        for i in range(self.galo.maxLife):
            dis.blit(self.interface['heartSprite'][1], (50 + (i * 35), 50))
        for i in range(self.galo.currentLife):
            dis.blit(self.interface['heartSprite'][0], (50 + (i * 35), 50))

    def events(self):
        if not self.galo.alive:
            self.run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                if event.key == pygame.K_d:
                    self.galo.setStatus(STT_WALKING)
                    self.galo.setDir(DIR_RIGTH)
                if event.key == pygame.K_a:
                    self.galo.setStatus(STT_WALKING)
                    self.galo.setDir(DIR_LEFT)
                if event.key == pygame.K_w:
                    if self.galo.collisionY(self.mundo):
                        self.galo.jumping = True
                        self.galo.setGravity(GRAVITY_JUMP)
                    elif self.galo.jumping:
                        self.galo.jumping = False
                        self.galo.setGravity(GRAVITY_SJUMP)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    if self.galo.dir == DIR_RIGTH:
                        self.galo.setStatus(STT_STOPED)
                if event.key == pygame.K_a:
                    if self.galo.dir == DIR_LEFT:
                        self.galo.setStatus(STT_STOPED)

    def checkIsRunning(self):
        return self.run

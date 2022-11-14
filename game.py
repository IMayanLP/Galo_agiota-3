import pygame
from random import random
from consts import *

from sky import Sky
from coin import Coin
from galo import Galo
from world import World
from button import Button
from camera import Camera
from enemies import Enemies
from spritesheet import SpriteSheet
from colision_box import Colision_box


class Game:
    def __init__(self):
        # spritesheets
        self.level = 1
        heart_ss = SpriteSheet(pygame.image.load('src/hearts.png').convert_alpha())
        botao_play = pygame.image.load('src/button.png').convert_alpha()
        botao_sair = pygame.image.load('src/buttonSair.png').convert_alpha()
        botao_retry = pygame.image.load('src/buttonRetry.png').convert_alpha()
        self.stage = MENU
        self.interface = {
            'heartSprite': [],
            'buttonPlay': Button(536, 300, botao_play),
            'buttonExit': Button(536, 400, botao_sair),
            'buttonRetry': Button(536, 300, botao_retry),
            'sky': None
        }
        for i in range(2):
            self.interface['heartSprite'].append(heart_ss.get_image(i, 0, SPRITE_SIZE, SPRITE_SIZE, 1, (0, 0, 0)))
        self.galo = None
        self.mundo = None
        self.cam = None
        self.inimigos = None
        self.coin = None
        self.run = True

    def gameInit(self):
        galo_ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
        slime_ss = SpriteSheet(pygame.image.load('src/spritesslime.png').convert_alpha())
        sky_ss = pygame.image.load('src/ceu1.png').convert_alpha()
        coin_ss = SpriteSheet(pygame.image.load('src/moedass.png').convert_alpha())
        self.sprites = [
            SpriteSheet(pygame.image.load('src/grama.png').convert_alpha()),
            SpriteSheet(pygame.image.load('src/terra.png').convert_alpha()),
            SpriteSheet(pygame.image.load('src/pedra.png').convert_alpha())
        ]
        self.galo = Galo(350, 0, ENTITIES_SIZE, ENTITIES_SIZE, 3, STT_STOPED, galo_ss, 4, 10, Colision_box(350, 350, 30, 30, 4 * SCALE, 8 * SCALE))
        self.mundo = World(101, 11, self.sprites, "map" + str(self.level) + ".json")
        self.interface['sky'] = Sky(sky_ss)
        self.cam = Camera(0, self.mundo.width * SPRITE_SIZE * SCALE, 2)
        self.inimigos = Enemies(int(random() * 10), slime_ss)
        self.coin = Coin(99 * SPRITE_SIZE * SCALE, 8 * SPRITE_SIZE * SCALE, ENTITIES_SIZE, ENTITIES_SIZE, 0, STT_STOPED, coin_ss, 1, 8, Colision_box(99 * SPRITE_SIZE * SCALE, 8 * SPRITE_SIZE * SCALE, ENTITIES_SIZE, ENTITIES_SIZE, 0, 0))

    def tick(self):
        if self.stage == IN_GAME:
            if self.coin.caught:
                self.nextLevel()
                self.gameInit()
            if self.galo.currentLife <= 0 or self.galo.colisionBox.x + self.galo.colisionBox.w < self.cam.displacement:
                self.stage = GAME_OVER
            self.cam.tick()
            self.interface['sky'].tick(self.cam)
            self.inimigos.tick(self.mundo, self.galo)
            self.galo.tick(self.mundo, self.inimigos)
            self.coin.tick(self.galo)

    def render(self, dis):
        if self.stage == MENU:
            dis.fill((50, 50, 50))
            self.interface['buttonPlay'].render(dis)
            self.interface['buttonExit'].render(dis)
        elif self.stage == IN_GAME:
            dis.fill((50, 50, 50))
            self.interface['sky'].render(dis)
            self.mundo.render(dis, self.cam)
            self.inimigos.render(dis, self.cam)
            self.galo.render(dis, self.cam)
            self.coin.render(dis, self.cam)
            for i in range(self.galo.maxLife):
                dis.blit(self.interface['heartSprite'][1], (50 + (i * 35), 50))
            for i in range(self.galo.currentLife):
                dis.blit(self.interface['heartSprite'][0], (50 + (i * 35), 50))
        elif self.stage == GAME_OVER:
            dis.fill((50, 50, 50))
            self.interface['buttonRetry'].render(dis)
            self.interface['buttonExit'].render(dis)

    def events(self):
        if self.galo is not None:
            if not self.galo.alive:
                self.stage = GAME_OVER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if self.stage == IN_GAME:
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
                            self.galo.gravity = GRAVITY_JUMP
                        elif self.galo.jumping:
                            self.galo.jumping = False
                            self.galo.gravity = GRAVITY_SJUMP
                    if event.key == pygame.K_o:
                        self.nextLevel()
                        self.gameInit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if self.stage == MENU:
                        if self.interface['buttonPlay'].click(x, y):
                            self.gameInit()
                            self.stage = IN_GAME
                        elif self.interface['buttonExit'].click(x, y):
                            self.run = False
                    elif self.stage == GAME_OVER:
                        if self.interface['buttonRetry'].click(x, y):
                            self.gameInit()
                            self.stage = IN_GAME
                        elif self.interface['buttonExit'].click(x, y):
                            self.run = False

            if event.type == pygame.KEYUP:
                if self.stage == IN_GAME:
                    if event.key == pygame.K_d:
                        if self.galo.dir == DIR_RIGTH:
                            self.galo.setStatus(STT_STOPED)
                    if event.key == pygame.K_a:
                        if self.galo.dir == DIR_LEFT:
                            self.galo.setStatus(STT_STOPED)

    def checkIsRunning(self):
        return self.run

    def nextLevel(self):
        if self.level == 2:
            self.level = 1
        else:
            self.level = 2
import pygame
from random import random
from consts import *

from sky import Sky
from coin import Coin
from galo import Galo
from world import World
from slime import Slime
from button import Button
from camera import Camera
from enemies import Enemies
from spritesheet import SpriteSheet
from colision_box import Colision_box


class Game:
    def __init__(self):
        self.level = 1

        self.menu_song = pygame.mixer.Sound('sounds/menu.mp3')
        self.menu_song.set_volume(0.5)
        self.menu_song.play(-1)

        self.game_song = pygame.mixer.Sound('sounds/ingame.mp3')
        self.game_song.set_volume(0.5)

        # spritesheets
        sky_ss = pygame.image.load('src/ceu1.png').convert_alpha()
        heart_ss = SpriteSheet(pygame.image.load('src/hearts.png').convert_alpha())
        botao_play = pygame.image.load('src/play1.png').convert_alpha()
        botao_play2 = pygame.image.load('src/play2.png').convert_alpha()
        botao_sair = pygame.image.load('src/exit1.png').convert_alpha()
        botao_sair2 = pygame.image.load('src/exit2.png').convert_alpha()
        botao_retry = pygame.image.load('src/retry1.png').convert_alpha()
        botao_retry2 = pygame.image.load('src/retry2.png').convert_alpha()
        botao_menu = pygame.image.load('src/menu1.png').convert_alpha()
        botao_menu2 = pygame.image.load('src/menu2.png').convert_alpha()
        botao_howPlay = pygame.image.load('src/howplay1.png').convert_alpha()
        botao_howPlay2 = pygame.image.load('src/howplay2.png').convert_alpha()
        botao_next = pygame.image.load('src/next1.png').convert_alpha()
        botao_next2 = pygame.image.load('src/next2.png').convert_alpha()
        title = pygame.image.load('src/title.png').convert_alpha()
        tour = pygame.image.load('src/tour.png').convert_alpha()
        self.interface = {
            'heartSprite': [],
            'buttonPlay': Button(536, 300, botao_play, botao_play2),
            'buttonExit': Button(536, 400, botao_sair, botao_sair2),
            'buttonRetry': Button(536, 300, botao_retry, botao_retry2),
            'buttonMenu': Button(536, 200, botao_menu, botao_menu2),
            'buttonNext': Button(536, 200, botao_next, botao_next2),
            'buttonHowPlay': Button(965, 600, botao_howPlay, botao_howPlay2),
            'Title': Button(420, -40, title, title),
            'Tour': Button(22, 10, tour, tour),
            'sky': Sky(sky_ss, 1)
        }
        for i in range(2):
            self.interface['heartSprite'].append(heart_ss.get_image(i, 0, SPRITE_SIZE, SPRITE_SIZE, 1, (0, 0, 0)))
        self.stage = MENU
        self.sprites = [
            SpriteSheet(pygame.image.load('src/grama.png').convert_alpha()),
            SpriteSheet(pygame.image.load('src/terra.png').convert_alpha()),
            SpriteSheet(pygame.image.load('src/pedra.png').convert_alpha())
        ]
        galo_ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
        self.galo = None
        self.mundo = None
        self.inimigos = None
        self.coin = None
        self.run = True
        self.menu_map = World(101, 11, self.sprites, "menu.json")
        self.cam = Camera(0, self.menu_map.width * SPRITE_SIZE * SCALE, 0)
        self.menu_galo = Galo(350, 0, ENTITIES_SIZE, ENTITIES_SIZE, 3, STT_WALKING, galo_ss, 6, 10, Colision_box(350, 350, 30, 30, 4 * SCALE, 8 * SCALE), SCALE)
        self.menu_galo.setStatus(STT_WALKING)
        self.menu_timer = 0
        self.tour_index = 0
        self.tour = self.tour = [
            "Utilize A e D para se movimentar",
            "Bom, agora utilize W para pular",
            "Use o W novamente enquanto está no ar e faça um double jump",
            "Agora pule encima dos inimigos para matá-los",
            "Eles dropam moedas, pege-as para ganhar pontos de agiotagem",
            "em jogo, ESC para pausar e O para passar de nível (cheat)"
        ]
        self.menu_slime = None
        self.menu_coin = None

    def gameInit(self):
        self.menu_song.stop()
        self.game_song.stop()
        galo_ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
        enemies_sprites = [
            SpriteSheet(pygame.image.load('src/spritesslime.png').convert_alpha()),
            SpriteSheet(pygame.image.load('src/moedass.png').convert_alpha())
        ]
        sky_ss = pygame.image.load('src/ceu1.png').convert_alpha()
        coin_ss = SpriteSheet(pygame.image.load('src/moedass.png').convert_alpha())
        self.galo = Galo(350, 0, ENTITIES_SIZE, ENTITIES_SIZE, self.level + 2, STT_STOPED, galo_ss, 4, 10, Colision_box(350, 350, 30, 30, 4 * SCALE, 8 * SCALE), SCALE)
        self.mundo = World(101, 11, self.sprites, "map" + str(self.level) + ".json")
        self.interface['sky'] = Sky(sky_ss, self.level * 3)
        self.cam = Camera(0, self.mundo.width * SPRITE_SIZE * SCALE, self.level + 0.5)
        self.inimigos = Enemies(int(random() * 10), enemies_sprites, 300 / self.level)
        self.coin = Coin(99 * SPRITE_SIZE * SCALE, 8 * SPRITE_SIZE * SCALE, ENTITIES_SIZE, ENTITIES_SIZE, 0, STT_STOPED, coin_ss, 1, 8, Colision_box(99 * SPRITE_SIZE * SCALE, 8 * SPRITE_SIZE * SCALE, ENTITIES_SIZE, ENTITIES_SIZE, 0, 0), SCALE)
        self.menu_song.stop()
        self.game_song.play(-1)

    def start_tour(self):
        slimes_ss = SpriteSheet(pygame.image.load('src/spritesslime.png').convert_alpha())
        coin_ss = SpriteSheet(pygame.image.load('src/moedass.png').convert_alpha())
        self.menu_slime = Slime(800, 0, ENTITIES_SIZE, ENTITIES_SIZE, 2, STT_STOPED, slimes_ss, 2, 10, Colision_box(800, 0, 30, 30, 4 * SCALE, 8 * SCALE), SCALE)
        self.menu_coin = Coin(800, 500, ENTITIES_SIZE, ENTITIES_SIZE, 0, STT_STOPED, coin_ss, 1, 8, Colision_box(800, 500, ENTITIES_SIZE / 2, ENTITIES_SIZE / 2, 0, 0), 1)
        self.tour_index = 0

    def tick(self):
        self.x, self.y = pygame.mouse.get_pos()
        if self.stage == IN_GAME:
            if self.coin.caught:
                self.stage = GAME_DONE
            if self.galo.currentLife <= 0 or self.galo.colisionBox.x + self.galo.colisionBox.w < self.cam.displacement or not self.galo.alive:
                self.stage = GAME_OVER
            self.cam.tick()
            self.interface['sky'].tick(self.cam)
            self.inimigos.tick(self.mundo, self.galo)
            self.coin.tick(self.galo)
            self.galo.tick(self.mundo, self.inimigos)

        elif self.stage == MENU:
            if self.menu_timer == 180:
                num = int(random() * 1000)
                if num % 3 == 0:
                    self.menu_galo.setStatus(STT_WALKING)
                    self.menu_galo.dir *= -1
                elif num % 3 == 1:
                    self.menu_galo.setStatus(STT_STOPED)
                else:
                    self.menu_galo.setStatus(STT_ANIMATING)
                self.menu_timer = 0
            else:
                self.menu_timer += 1
            if self.menu_galo.colisionBox.x + self.menu_galo.colisionBox.w + self.menu_galo.vel >= SCREEN_WIDTH:
                self.menu_galo.setDir(DIR_LEFT)
            if self.menu_galo.x - self.menu_galo.vel <= 0:
                self.menu_galo.setDir(DIR_RIGTH)
            self.cam.tick()
            self.interface['sky'].tick(self.cam)
            self.menu_galo.tick(self.menu_map, self.inimigos)

        elif self.stage == GAME_TOUR:
            if self.menu_slime.deadTimer > 60:
                self.menu_slime.y = 700
                self.menu_coin.tick(self.menu_galo)
            if self.menu_galo.check_Collision(self.menu_slime) and self.menu_galo.gravity > 0 and self.tour_index == 3:
                self.menu_slime.alive = False
                self.menu_galo.setGravity(GRAVITY_SJUMP)
                self.tour_index += 1
            if self.menu_coin.caught and self.tour_index == 4:
                self.tour_index += 1
            self.interface['sky'].tick(self.cam)
            self.menu_slime.tick(self.menu_map, self.menu_galo)
            self.menu_galo.tick(self.menu_map, self.inimigos)

    def render(self, dis, font):
        if self.stage == MENU:
            dis.fill((50, 50, 50))
            self.interface['sky'].render(dis)
            self.menu_map.render(dis, self.cam)
            self.menu_galo.render(dis, self.cam)
            self.interface['buttonPlay'].render(dis)
            self.interface['buttonExit'].render(dis)
            self.interface['buttonHowPlay'].render(dis)
            self.interface['Title'].render(dis)
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
        elif self.stage == GAME_PAUSED:
            dis.fill((50, 50, 50))
            self.interface['sky'].render(dis)
            self.mundo.render(dis, self.cam)
            self.inimigos.render(dis, self.cam)
            self.galo.render(dis, self.cam)
            self.coin.render(dis, self.cam)
            self.interface['buttonPlay'].render(dis)
            self.interface['buttonMenu'].render(dis)
            self.interface['buttonExit'].render(dis)
        elif self.stage == GAME_OVER:
            dis.fill((50, 50, 50))
            text = font.render('Score: ' + str(self.galo.score), True, (255, 255, 255))
            if self.galo.score > 9:
                dis.blit(text, (530, 230))
            else:
                dis.blit(text, (535, 230))
            self.interface['buttonRetry'].render(dis)
            self.interface['buttonExit'].render(dis)
        elif self.stage == GAME_DONE:
            dis.fill((50, 50, 50))
            text = font.render('Score: ' + str(self.galo.score), True, (255, 255, 255))
            if self.galo.score > 9:
                dis.blit(text, (530, 140))
            else:
                dis.blit(text, (535, 140))
            if self.level == 1:
                self.interface['buttonNext'].render(dis)
            else:
                self.interface['buttonMenu'].render(dis)
            self.interface['buttonRetry'].render(dis)
            self.interface['buttonExit'].render(dis)
        elif self.stage == GAME_TOUR:
            dis.fill((50, 50, 50))
            self.interface['sky'].render(dis)
            self.menu_map.render(dis, self.cam)
            self.menu_slime.render(dis, self.cam)
            self.menu_galo.render(dis, self.cam)
            if self.menu_slime.deadTimer > 60 and self.tour_index == 4:
                self.menu_coin.render(dis, self.cam)
            self.interface['Tour'].render(dis)
            text = font.render(self.tour[self.tour_index], True, (255, 255, 255))
            dis.blit(text, (35, 25))
            if self.tour_index == 5:
                self.interface['buttonMenu'].render(dis)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if self.stage == IN_GAME:
                    if event.key == pygame.K_ESCAPE:
                        self.stage = GAME_PAUSED
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
                        self.stage = GAME_DONE

                if self.stage == GAME_TOUR:
                    if event.key == pygame.K_d:
                        self.menu_galo.setStatus(STT_WALKING)
                        self.menu_galo.setDir(DIR_RIGTH)
                    if event.key == pygame.K_a:
                        self.menu_galo.setStatus(STT_WALKING)
                        self.menu_galo.setDir(DIR_LEFT)
                    if event.key == pygame.K_w:
                        if self.menu_galo.collisionY(self.menu_map):
                            self.menu_galo.jumping = True
                            self.menu_galo.gravity = GRAVITY_JUMP
                            if self.tour_index == 1:
                                self.tour_index += 1
                        elif self.menu_galo.jumping:
                            self.menu_galo.jumping = False
                            self.menu_galo.gravity = GRAVITY_SJUMP
                            if self.tour_index == 2:
                                self.tour_index += 1

            if event.type == pygame.KEYUP:
                if self.stage == IN_GAME:
                    if event.key == pygame.K_d:
                        if self.galo.dir == DIR_RIGTH:
                            self.galo.setStatus(STT_STOPED)
                    if event.key == pygame.K_a:
                        if self.galo.dir == DIR_LEFT:
                            self.galo.setStatus(STT_STOPED)

                if self.stage == GAME_TOUR:
                    if event.key == pygame.K_d:
                        if self.menu_galo.dir == DIR_RIGTH:
                            self.menu_galo.setStatus(STT_STOPED)
                            if self.tour_index == 0:
                                self.tour_index += 1
                    if event.key == pygame.K_a:
                        if self.menu_galo.dir == DIR_LEFT:
                            self.menu_galo.setStatus(STT_STOPED)
                            if self.tour_index == 0:
                                self.tour_index += 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.stage == MENU:
                        if self.interface['buttonPlay'].click(self.x, self.y):
                            self.interface['buttonPlay'].pressed = True
                        elif self.interface['buttonHowPlay'].click(self.x, self.y):
                            self.interface['buttonHowPlay'].pressed = True
                    elif self.stage == GAME_OVER:
                        if self.interface['buttonRetry'].click(self.x, self.y):
                            self.interface['buttonRetry'].pressed = True
                    elif self.stage == GAME_PAUSED:
                        if self.interface['buttonMenu'].click(self.x, self.y):
                            self.interface['buttonMenu'].pressed = True
                        elif self.interface['buttonPlay'].click(self.x, self.y):
                            self.interface['buttonPlay'].pressed = True
                    elif self.stage == GAME_DONE:
                        if self.level == 1:
                            if self.interface['buttonNext'].click(self.x, self.y):
                                self.interface['buttonNext'].pressed = True
                        else:
                            if self.interface['buttonMenu'].click(self.x, self.y):
                                self.interface['buttonMenu'].pressed = True
                        if self.interface['buttonRetry'].click(self.x, self.y):
                            self.interface['buttonRetry'].pressed = True
                    elif self.stage == GAME_TOUR:
                        if self.tour_index == 5:
                            if self.interface['buttonMenu'].click(self.x, self.y):
                                self.interface['buttonMenu'].pressed = True

                    if self.stage != IN_GAME:
                        if self.interface['buttonExit'].click(self.x, self.y):
                            self.interface['buttonExit'].pressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                    if self.stage == MENU:
                        if self.interface['buttonPlay'].click(self.x, self.y) and self.interface['buttonPlay'].pressed:
                            self.interface['buttonPlay'].pressed = False
                            self.level = 1
                            self.gameInit()
                            self.stage = IN_GAME
                        elif self.interface['buttonHowPlay'].click(self.x, self.y) and self.interface['buttonHowPlay'].pressed:
                            self.interface['buttonHowPlay'].pressed = False
                            self.menu_galo.setStatus(STT_STOPED)
                            self.start_tour()
                            self.stage = GAME_TOUR
                    elif self.stage == GAME_OVER:
                        if self.interface['buttonRetry'].click(self.x, self.y) and self.interface['buttonRetry'].pressed:
                            self.interface['buttonRetry'].pressed = False
                            self.gameInit()
                            self.stage = IN_GAME
                    elif self.stage == GAME_PAUSED:
                        if self.interface['buttonMenu'].click(self.x, self.y) and self.interface['buttonMenu'].pressed:
                            self.interface['buttonMenu'].pressed = False
                            self.cam = Camera(0, self.menu_map.width * SPRITE_SIZE * SCALE, 0)
                            self.game_song.stop()
                            self.menu_song.play(-1)
                            self.stage = MENU
                        elif self.interface['buttonPlay'].click(self.x, self.y) and self.interface['buttonPlay'].pressed:
                            self.interface['buttonPlay'].pressed = False
                            self.galo.setStatus(STT_STOPED)
                            self.stage = IN_GAME
                    elif self.stage == GAME_DONE:
                        if self.level == 1:
                            if self.interface['buttonNext'].click(self.x, self.y) and self.interface['buttonNext'].pressed:
                                self.interface['buttonNext'].pressed = False
                                self.nextLevel()
                                self.stage = IN_GAME
                        else:
                            if self.interface['buttonMenu'].click(self.x, self.y) and self.interface['buttonMenu'].pressed:
                                self.interface['buttonMenu'].pressed = False
                                self.game_song.stop()
                                self.menu_song.play(-1)
                                self.cam = Camera(0, self.menu_map.width * SPRITE_SIZE * SCALE, 0)
                                self.stage = MENU
                        if self.interface['buttonRetry'].click(self.x, self.y) and self.interface['buttonRetry'].pressed:
                            self.interface['buttonRetry'].pressed = False
                            self.gameInit()
                            self.stage = IN_GAME
                    elif self.stage == GAME_TOUR:
                        if self.tour_index == 5:
                            if self.interface['buttonMenu'].click(self.x, self.y) and self.interface['buttonMenu'].pressed:
                                self.interface['buttonMenu'].pressed = False
                                self.tour_index = 0
                                self.cam = Camera(0, self.menu_map.width * SPRITE_SIZE * SCALE, 0)
                                self.stage = MENU

                    if self.stage != IN_GAME:
                        if self.interface['buttonExit'].click(self.x, self.y) and self.interface['buttonExit'].pressed:
                            self.interface['buttonExit'].pressed = False
                            self.run = False

    def checkIsRunning(self):
        return self.run

    def nextLevel(self):
        if self.level == 1:
            self.level = 2
            self.gameInit()

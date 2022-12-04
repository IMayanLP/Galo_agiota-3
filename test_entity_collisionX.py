import pytest
from game import *


def run_game():
    pygame.init()
    dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Game()
    game.gameInit()
    return game


def test_01_true():
    jogo = run_game()
    jogo.galo.x = jogo.mundo.width * SPRITE_SIZE * SCALE
    jogo.galo.y = 0
    jogo.galo.status = STT_WALKING
    jogo.galo.dir = DIR_RIGTH
    jogo.galo.colisionBox.update(jogo.galo.x, jogo.galo.y)
    assert jogo.galo.collisionY(jogo.mundo) is True


def test_02_true():
    jogo = run_game()
    jogo.galo.x = (16 * SPRITE_SIZE * SCALE) + 16
    jogo.galo.y = 10 * SPRITE_SIZE * SCALE
    jogo.galo.status = STT_WALKING
    jogo.galo.dir = DIR_RIGTH
    jogo.galo.colisionBox.update(jogo.galo.x, jogo.galo.y)
    assert jogo.galo.collisionY(jogo.mundo) is True


def test_03_false():
    jogo = run_game()
    jogo.galo.x = 0
    jogo.galo.y = 0
    jogo.galo.status = STT_WALKING
    jogo.galo.dir = DIR_RIGTH
    jogo.galo.colisionBox.update(jogo.galo.x, jogo.galo.y)
    assert jogo.galo.collisionY(jogo.mundo) is False

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
    jogo.galo.gravity = 100
    jogo.galo.x = 11 * SPRITE_SIZE * SCALE
    jogo.galo.y = jogo.mundo.height * SPRITE_SIZE * SCALE
    jogo.galo.colisionBox.update(jogo.galo.x, jogo.galo.y)
    assert jogo.galo.collisionY(jogo.mundo) is True


def test_02_true():
    jogo = run_game()
    jogo.galo.gravity = 0
    jogo.galo.x = 0
    jogo.galo.y = 11 * SPRITE_SIZE * SCALE
    jogo.galo.colisionBox.update(jogo.galo.x, jogo.galo.y)
    assert jogo.galo.collisionY(jogo.mundo) is True


def test_03_false():
    jogo = run_game()
    jogo.galo.gravity = 0
    jogo.galo.x = 0
    jogo.galo.y = 0
    jogo.galo.colisionBox.update(jogo.galo.x, jogo.galo.y)
    assert jogo.galo.collisionY(jogo.mundo) is False

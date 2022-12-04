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
    jogo.run = True
    assert jogo.checkIsRunning() is True


def test_01_false():
    jogo = run_game()
    jogo.run = False
    assert jogo.checkIsRunning() is False

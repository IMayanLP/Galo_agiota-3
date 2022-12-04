import pytest
import pygame
from button import *


def run_button():
    pygame.init()
    dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    b_play = pygame.image.load('src/play1.png').convert_alpha()
    b_play2 = pygame.image.load('src/play2.png').convert_alpha()
    b_test = Button(0, 0, b_play, b_play2)
    return b_test


def test_01_true():
    b_test = run_button()
    x = 0
    y = 0
    assert b_test.click(x, y) is True


def test_02_false():
    b_test = run_button()
    x = b_test.colisionBox.width + 10
    y = b_test.colisionBox.height + 10
    assert b_test.click(x, y) is False

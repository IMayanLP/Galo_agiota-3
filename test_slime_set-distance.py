import pytest
from game import *


def run_slime():
    pygame.init()
    dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    slimes_ss = SpriteSheet(pygame.image.load('src/spritesslime.png').convert_alpha())
    galo_ss = SpriteSheet(pygame.image.load('src/spritesgalo.png').convert_alpha())
    slime_test = Slime(0, 0, ENTITIES_SIZE, ENTITIES_SIZE, 2, STT_STOPED, slimes_ss, 2, 10, Colision_box(0, 0, 30, 30, 4 * SCALE, 8 * SCALE), SCALE)
    galo_test = Galo(60, 0, ENTITIES_SIZE, ENTITIES_SIZE, 3, STT_STOPED, galo_ss, 4, 10, Colision_box(60, 0, 30, 30, 4 * SCALE, 8 * SCALE), SCALE)
    return slime_test, galo_test


def test_01_60():
    slime_test, galo_test = run_slime()
    assert slime_test.set_distance(galo_test) == 60


def test_02_60():
    slime_test, galo_test = run_slime()
    slime_test.x = 120
    assert slime_test.set_distance(galo_test) == 60

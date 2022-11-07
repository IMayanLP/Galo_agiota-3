import pygame


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, line, w, h, scale, color):
        img = pygame.Surface((w, h)).convert_alpha()
        img.blit(self.sheet, (0, 0), ((frame * w), (line * h), w, h))
        img = pygame.transform.scale(img, (w * scale, h * scale))
        img.set_colorkey(color)
        return img
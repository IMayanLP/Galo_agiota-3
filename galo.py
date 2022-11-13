from entity import Entity
from consts import *


class Galo(Entity):
    gravity = 0

    def setStatus(self, newStatus):
        self.status = newStatus
        self.frame = 0

    def setDir(self, newDir):
        self.dir = newDir

    def tick(self):
        if self.status == STT_WALKING:
            self.x += self.vel * self.dir

        self.gravity += 1
        self.y += self.gravity

        if self.colidiu():
            self.y = SCREEN_HEIGHT - (self.h * SCALE)

        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += 0.2

    def render(self, display):
        if self.status == STT_WALKING:
            if self.dir == DIR_RIGTH: display.blit(self.ss[0][int(self.frame)], (self.x, self.y))
            else: display.blit(self.ss[1][int(self.frame)], (self.x, self.y))

        elif self.status == STT_STOPED:
            if self.dir == DIR_RIGTH: display.blit(self.ss[2][int(self.frame)], (self.x, self.y))
            else: display.blit(self.ss[3][int(self.frame)], (self.x, self.y))

    def colidiu(self):
        if self.y + (self.h * SCALE) >= SCREEN_HEIGHT: return True
        else: return False

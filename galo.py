from entity import *
from consts import *


class Galo(Entity):
    def setStatus(self, newStatus):
        self.status = newStatus

    def setDir(self, newDir):
        self.dir = newDir

    def tick(self):
        if self.status == STT_WALKING:
            self.x += self.vel * self.dir

        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += 0.2

    def render(self, display):
        if self.status == STT_WALKING:
            if self.dir == DIR_RIGTH:
                display.blit(self.ss[0][int(self.frame)], (self.x, self.y))
            else:
                display.blit(self.ss[1][int(self.frame)], (self.x, self.y))

        elif self.status == STT_STOPED:
            if self.dir == DIR_RIGTH:
                display.blit(self.ss[0][0], (self.x, self.y))
            else:
                display.blit(self.ss[1][0], (self.x, self.y))

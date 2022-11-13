import pygame
from entity import Entity
from consts import *


class Galo(Entity):
    gravity = 0
    jumping = False

    def setStatus(self, newStatus):
        self.status = newStatus
        self.frame = 0

    def setDir(self, newDir):
        self.dir = newDir

    def setGravity(self, newGravity):
        self.gravity = newGravity

    def tick(self, world, enemies):
        self.colisionBox.update(self.x, self.y)
        if self.status == STT_WALKING:
            if not self.collisionX(world):
                self.x += self.vel * self.dir

        if not self.collisionY(world):
            self.gravity += 1
            self.y += self.gravity
        else:
            self.jumping = False
            self.setGravity(0)

        self.enemies_Collision(enemies)

        if self.frame > len(self.ss[self.status]) - 1:
            self.frame = 0
        else:
            self.frame += 0.2

    def render(self, display, camera):
        if self.status == STT_WALKING:
            if self.dir == DIR_RIGTH: display.blit(self.ss[0][int(self.frame)], (self.x - camera.displacement, self.y))
            else: display.blit(self.ss[1][int(self.frame)], (self.x - camera.displacement, self.y))

        elif self.status == STT_STOPED:
            if self.dir == DIR_RIGTH: display.blit(self.ss[2][int(self.frame)], (self.x - camera.displacement, self.y))
            else: display.blit(self.ss[3][int(self.frame)], (self.x - camera.displacement, self.y))

    def enemies_Collision(self, e):
        x0 = self.colisionBox.x
        x1 = self.colisionBox.x + self.colisionBox.w
        y1 = self.colisionBox.y + self.colisionBox.h
        for i in range(len(e.enemies['slimes'])):
            if e.enemies['slimes'][i] is not None:
                if self.is_Colliding(x0, y1,
                                     e.enemies['slimes'][i].colisionBox.x,
                                     e.enemies['slimes'][i].colisionBox.x + e.enemies['slimes'][i].colisionBox.w,
                                     e.enemies['slimes'][i].colisionBox.y,
                                     e.enemies['slimes'][i].colisionBox.y + e.enemies['slimes'][i].colisionBox.h) \
                        or self.is_Colliding(x1, y1,
                                             e.enemies['slimes'][i].colisionBox.x,
                                             e.enemies['slimes'][i].colisionBox.x + e.enemies['slimes'][i].colisionBox.w,
                                             e.enemies['slimes'][i].colisionBox.y,
                                             e.enemies['slimes'][i].colisionBox.y + e.enemies['slimes'][i].colisionBox.h):
                    if self.gravity > 0 and e.enemies['slimes'][i].dead == False:
                        self.gravity = GRAVITY_SJUMP
                        self.jumping = False
                        e.enemies['slimes'][i].dead = True

    def is_Colliding(self, p0, p1, x0, x1, y0, y1):
        if x0 <= p0 <= x1 and y0 <= p1 <= y1:
            return True
        return False

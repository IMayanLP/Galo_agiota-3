import pygame
from entity import Entity
from consts import *


class Galo(Entity):
    maxLife = 3
    currentLife = maxLife
    invulnerable = 60
    gravity = NO_GRAVITY
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

        if enemies is not None:
            self.enemies_Collision(enemies)

        if self.invulnerable < 60:
            self.invulnerable += 1

        self.animate()

    def render(self, display, camera):
        if self.status == STT_WALKING:
            if self.dir == DIR_RIGTH: display.blit(self.ss[0][int(self.frame)], (self.x - camera.displacement, self.y))
            else: display.blit(self.ss[1][int(self.frame)], (self.x - camera.displacement, self.y))

        elif self.status == STT_STOPED:
            if self.dir == DIR_RIGTH: display.blit(self.ss[2][int(self.frame)], (self.x - camera.displacement, self.y))
            else: display.blit(self.ss[3][int(self.frame)], (self.x - camera.displacement, self.y))

        elif self.status == STT_ANIMATING:
            if self.dir == DIR_RIGTH: display.blit(self.ss[4][int(self.frame)], (self.x - camera.displacement, self.y))
            else: display.blit(self.ss[5][int(self.frame)], (self.x - camera.displacement, self.y))

    def enemies_Collision(self, e):
        for i in range(len(e.enemies['slimes'])):
            if e.enemies['slimes'][i] is not None:
                if self.check_Collision(e.enemies['slimes'][i]):
                    if self.gravity > 0 and e.enemies['slimes'][i].alive:
                        self.setGravity(GRAVITY_SJUMP)
                        self.jumping = False
                        e.enemies['slimes'][i].alive = False
                    elif self.invulnerable == 60 and e.enemies['slimes'][i].alive:
                        self.currentLife -= e.enemies['slimes'][i].damage
                        self.invulnerable = 0

    def is_Colliding(self, p0, p1, x0, x1, y0, y1):
        if x0 <= p0 <= x1 and y0 <= p1 <= y1:
            return True
        return False

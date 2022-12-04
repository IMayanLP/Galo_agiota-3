from entity import Entity
from consts import *


class Galo(Entity):
    score = 0
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
        display.blit(self.ss[self.get_ss_line()][int(self.frame)], (self.x - camera.displacement, self.y))

    def get_ss_line(self):
        return self.get_dir() + (self.status * 2)

    def get_dir(self):
        if self.dir == DIR_RIGTH:
            return 0
        else:
            return 1

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

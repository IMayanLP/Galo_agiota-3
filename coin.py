from entity import Entity


class Coin(Entity):
    caught = False

    def tick(self, galo):
        if self.check_Collision(galo):
            self.caught = True
        self.animate()

    def render(self, display, camera):
        display.blit(self.ss[0][int(self.frame)], (self.x - camera.displacement, self.y))

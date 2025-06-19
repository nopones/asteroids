import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self,screen):
        color=(255,0,0)
        center=(int(self.position.x),int(self.position.y))
        pygame.draw.circle(screen,color,center,self.radius,width=2)

    def update(self, dt):
        self.position+=self.velocity*dt
        # sub-classes must override
        pass

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            angle=random.uniform(20,50)
            ast1_angle=self.velocity.rotate(angle)
            ast2_angle=self.velocity.rotate(-angle)
            ast_radius=self.radius-ASTEROID_MIN_RADIUS
            ast1=Asteroid(self.position.x,self.position.y,ast_radius)
            ast1.velocity=ast1_angle*1.2
            ast2=Asteroid(self.position.x,self.position.y,ast_radius)
            ast2.velocity=ast2_angle*1.2


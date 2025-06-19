import pygame
from circleshape import CircleShape
from shooting import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.timer=0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        white=(255,255,255)
        pygame.draw.polygon(screen,white,self.triangle(),2)

    def rotate(self,dt):
        self.rotation+=PLAYER_TURN_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer-=dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        pass

    def shoot(self):
        if self.timer<0:
            bullet=Shot(self.position.x,self.position.y,SHOT_RADIUS)
            start = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = start * PLAYER_SHOOT_SPEED
            self.timer=PLAYER_SHOOT_COOLDOWN
        else:
            pass

        
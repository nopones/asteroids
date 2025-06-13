# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED, 
)    

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #as2=Asteroid(100.1,180,2)
    #as1=Asteroid(100.9,199.2,2)
    player=Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    asteroid_field=AsteroidField()
    

    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    clock=pygame.time.Clock()
    dt=0

    black= (0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        for item in drawable:
            item.draw(screen)
        
        for item in updatable:
            item.update(dt)

        for ast in asteroids:
            if ast.collision(player)==True:
                print ("Game Over")
                return
        pygame.display.flip()
        dt=clock.tick(60)/1000
        
        #dt=(pygame.tick(60)/1000)

if __name__ == "__main__":
    main()
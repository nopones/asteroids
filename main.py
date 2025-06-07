# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
)    

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player=Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
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
        player.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000
        
        #dt=(pygame.tick(60)/1000)

if __name__ == "__main__":
    main()
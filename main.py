import pygame
import random
from constants import *
from circleshape import *
from player import *
from asteroid import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        

        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
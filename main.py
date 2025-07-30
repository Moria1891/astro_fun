# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroidfield = pygame.sprite.Group()
shots = pygame.sprite.Group()


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    # print(f"AsteroidField created. updatable group has {len(updatable)} sprites")
    # print(f"Sprites in updatable: {[type(sprite).__name__ for sprite in updatable]}")
    clock = pygame.time.Clock()
    dt = 0
    


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt)    
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                running = False
                sys.exit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    asteroid.kill()

        screen.fill(BLACK)
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()

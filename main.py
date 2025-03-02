from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

import pygame
import constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroid_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = [updatable_group]
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        screen.fill('black')
        updatable_group.update(dt)
        for obj in drawable_group:
            obj.draw(screen)
        for obj in asteroid_group:
            if obj.collided_with(player):
                print('Game Over!')
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        time_elapsed = clock.tick(60)
        dt = time_elapsed / 1000.0


if __name__ == '__main__':
    main()

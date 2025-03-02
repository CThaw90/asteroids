from player import Player

import pygame
import constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    player.containers = (updatable_group, drawable_group)

    while True:
        screen.fill('black')
        updatable_group.update(dt)
        for obj in drawable_group:
            obj.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        time_elapsed = clock.tick(60)
        dt = time_elapsed / 1000.0


if __name__ == '__main__':
    main()

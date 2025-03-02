from player import Player

import pygame
import constants

def main():
    print('Starting Asteroids!')
    print('Screen width:', constants.SCREEN_WIDTH)
    print('Screen height:', constants.SCREEN_HEIGHT)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    while True:
        screen.fill('black')
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        time_elapsed = clock.tick(60)
        dt = time_elapsed / 1000.0


if __name__ == '__main__':
    main()

import pygame
import constants

def main():
    print('Starting Asteroids!')
    print('Screen width:', constants.SCREEN_WIDTH)
    print('Screen height:', constants.SCREEN_HEIGHT)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()


if __name__ == '__main__':
    main()

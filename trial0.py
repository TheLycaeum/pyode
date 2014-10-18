import pygame
from pygame.locals import Rect, DOUBLEBUF

X_MAX, Y_MAX = 1024, 768

everything = pygame.sprite.Group()


def main():
    screen = pygame.display.set_mode((X_MAX, Y_MAX), DOUBLEBUF)
    empty = pygame.Surface((X_MAX, Y_MAX))
    clock = pygame.time.Clock() 

    while True:
        clock.tick(30)
        everything.clear(screen, empty)
        everything.update()
        everything.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    import sys
    sys.exit(main())

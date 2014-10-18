import pygame
from pygame.locals import Rect, DOUBLEBUF

X_MAX, Y_MAX = 1024, 768

everything = pygame.sprite.Group()

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size = 20):
        super(Ball, self).__init__()
        self.image = pygame.Surface((size * 2, size * 2)).convert()
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (200, 0, 200), (size, size), size, 0)

        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.velocity = 5
        self.add(everything)
    
    def update(self):
        x, y = self.rect.center

        y += self.velocity
        if y >= Y_MAX or y <= 0:
            self.velocity *= -1

        self.rect.center = x, y

            
        
    

def main():
    screen = pygame.display.set_mode((X_MAX, Y_MAX), DOUBLEBUF)
    empty = pygame.Surface((X_MAX, Y_MAX))
    clock = pygame.time.Clock() 
    b = Ball(X_MAX/2, 10)

    while True:
        clock.tick(30)
        everything.clear(screen, empty)
        everything.update()
        everything.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    import sys
    sys.exit(main())

import ode
import pygame
from pygame.locals import Rect, DOUBLEBUF

SCALE = 4.0

X_MAX, Y_MAX = 512, 512

everything = pygame.sprite.Group()

def g_to_w(x, y, z):
    "Converts the x,y and z coordinates from graphics to world (pygame to ODE)"
    rx = (x - 256)/SCALE
    ry = (256 - y)/SCALE
    rz = 0
    return (rx, ry, rz)

    
def w_to_g(x, y, z):
    "Converts the x,y and z coordinates from world to graphics (ODE to pygame)"
    rx = SCALE*x + 256
    ry = 256 - SCALE*y
    rz = 0
    return (rx, ry, rz)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, world, space, size = 20):
        super(Ball, self).__init__()
        self.image = pygame.Surface((size * 2, size * 2)).convert()
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (200, 0, 200), (size, size), size, 0)

        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.velocity = 5
        self.add(everything)

        mass = ode.Mass()
        mass.setSphere(100, size/SCALE) 

        self.body = ode.Body(world)
        self.body.setMass(mass)
        self.body.setPosition(g_to_w(x, y, 0))

        self.geom = ode.GeomSphere(space, size/SCALE) # Radius is 15
        self.geom.setBody(self.body)

    
    def update(self):
        x, y, z = w_to_g(*self.body.getPosition())
        self.rect.center = x, y

def create_world():
    "Creates the world and related components"
    world = ode.World()
    world.setGravity( (0, -9.81, 0) )
    world.setERP(0.8) # Error reduction parameter
    world.setCFM(1E-5) # Constraint Force Mixing
    return world
        


def near_callback(args, g0, g1):
    contacts = ode.collide(g0, g1)
    world, contactgroup = args
    for c in contacts:
        # Various collision parameters can be set here
        # c.setBounce(0.9)
        j = ode.ContactJoint(world, contactgroup, c)
        j.attach(g0.getBody(), g1.getBody())
    

def main():
    screen = pygame.display.set_mode((X_MAX, Y_MAX), DOUBLEBUF)
    empty = pygame.Surface((X_MAX, Y_MAX))
    clock = pygame.time.Clock() 

    world = create_world()
    space = ode.Space()
    floor = ode.GeomPlane(space, (0, 1, 0), -15)
    contactgroup = ode.JointGroup()        

    b = Ball(X_MAX/2, 10, world, space)

    fps = 30
    iters_per_frame = 10
    dt = 1.0/fps 



    while True:
        clock.tick(fps)

        for i in range(iters_per_frame):
            space.collide((world, contactgroup), near_callback)
            world.step(dt)
            contactgroup.empty()


        everything.clear(screen, empty)
        everything.update()
        everything.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    import sys
    sys.exit(main())

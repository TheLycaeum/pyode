import ode

def create_world():
    "Creates the world and related components"
    world = ode.World()
    world.setGravity( (0, -9.81, 0) )
    world.setERP(0.8) # Error reduction parameter
    world.setCFM(1E-5) # Constraint Force Mixing
    return world


def main():
    world = create_world()


    mass = ode.Mass()
    mass.setSphere(10, 15) # Density 10 and radius 15

    body = ode.Body(world)
    body.setMass(mass)
    body.setPosition((10, 100 , 0))

    prev = body.getPosition()[1]

    for i in range(100):
        world.step(0.1)
        current = body.getPosition()[1]
        print "{:10} {:10}".format(current, current-prev)
        prev = current





if __name__ == '__main__':
    import sys
    sys.exit(main())

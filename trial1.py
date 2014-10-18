import ode

def create_world():
    "Creates the world and related components"
    world = ode.World()
    world.setGravity( (0, -9.81, 0) )
    world.setERP(0.8) # Error reduction parameter
    world.setCFM(1E-5) # Constraint Force Mixing
    return world

def near_callback(args, g0, g1):
    print "Click!"
    contacts = ode.collide(g0, g1)
    world, contactgroup = args
    for c in contacts:
        # Various collision parameters can be set here
        j = ode.ContactJoint(world, contactgroup, c)
        j.attach(g0.getBody(), g1.getBody())


def main():
    world = create_world()

    # Rigid body dynamics
    mass = ode.Mass()
    mass.setSphere(10, 15) # Density 10 and radius 15

    body = ode.Body(world)
    body.setMass(mass)
    body.setPosition((10, 100 , 0))

    # Collision detection
    space = ode.Space()
    ## Floor
    floor = ode.GeomPlane(space, (0, 1, 0), 5)
    ## Sphere
    geom = ode.GeomSphere(space, 15) # Radius is 15
    geom.setBody(body)
    contactgroup = ode.JointGroup()    

    prev = body.getPosition()[1]

    for i in range(100):
        space.collide((world, contactgroup), near_callback)
        world.step(0.1)
        contactgroup.empty()

        current = body.getPosition()[1]
        print "{:10} {:10}".format(current, current-prev)
        prev = current





if __name__ == '__main__':
    import sys
    sys.exit(main())

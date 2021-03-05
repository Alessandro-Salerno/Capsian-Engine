from Capsian import *
from addons  import *


# Initial stuff
camera  = PerspectiveCamera(Transform(0, 5, 5, 0, 0, 0, 10, -90))
controller = CharacterController()
camera.components.add(controller)
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)

tex = Texture3D("assets/textures/glass.png")
mat = Material(texture=tex)
s = Scene3D(camera)
o = OverlayScene(camera)
# Label3D(font="calibri", font_size=36, transform=Transform(0, 0, 0, None, None, None), text=s.drawable.__len__, color=Color(255, 255, 255).rgba, scene=o)
# Label3D(font="calibri", font_size=36, transform=Transform(100, 0, 0, None, None, None), text=s.objects2D.__len__, color=Color(255, 255, 255).rgba, scene=o)
# Label3D(font="calibri", font_size=36, transform=Transform(200, 0, 0, None, None, None), text=s.stack.__len__, color=Color(255, 255, 255).rgba, scene=o)
FPSCounter(o)


class Keyboard(KeyboardInputHandler):
    def on_key_held(self, keys):
        if keys[Key.S]:
            controller.move("backwards")

        if keys[Key.A]:
            controller.move("left")

        if keys[Key.D]:
            controller.move("right")

        if keys[Key.W]:
            controller.move("forwards")

        if keys[Key.SPACE]:
            controller.move(Direction.UP)

        if keys[Key.LSHIFT]:
            controller.move(Direction.DOWN)


camera.components.add(Keyboard())


# Map
Cube(Transform(0, 0, 0, 10, 1, 10), s, mat)
l1 = AmbientLight(Color(0, 255, 0).rgba)
l2 = AmbientLight(Color(255, 0, 0).rgba)
l3 = AmbientLight(Color(0, 0, 255).rgba)
l4 = AmbientLight(Color(255, 0, 255).rgba)

l5 = AmbientLight(Color(50, 0, 0).rgba)
l6 = AmbientLight(Color(0, 50, 0).rgba)
l7 = AmbientLight(Color(50, 0, 50).rgba)
l8 = AmbientLight(Color(0, 0, 50).rgba)


Entity(Transform(0, 25, 5), s).components.add(l1)
Entity(Transform(10, 25, 5), s).components.add(l2)
Entity(Transform(10, 25, 15), s).components.add(l3)
Entity(Transform(0, 25, 15), s).components.add(l4)

Entity(Transform(0, 2, 0), s).components.add(l5)
Entity(Transform(10, 2, 0), s).components.add(l6)
Entity(Transform(10, 2, 10), s).components.add(l7)
Entity(Transform(0, 2, 10), s).components.add(l8)


def gen_particles(dt):
    Particles3D(
         transform=Transform(
            5, 2, 5,
            0.50,
            0.50,
            0,
            dy=1
        ),

        amount=1,
        duration=50,
        scene=s
    )

    Particles3D(
         transform=Transform(
            5, 2, 5,
            0.50,
            0.50,
            0,
            dx=-2,
            dy=5
        ),

        amount=1,
        duration=10,
        scene=s
    )

    Particles3D(
         transform=Transform(
            5, 2, 5,
            0.50,
            0.50,
            0,
            dx=2,
            dy=5
        ),

        amount=1,
        duration=10,
        scene=s
    )

    Particles3D(
         transform=Transform(
            5, 2, 5,
            0.50,
            0.50,
            0,
            dz=-2,
            dy=5
        ),

        amount=1,
        duration=10,
        scene=s
    )

    Particles3D(
         transform=Transform(
            5, 2, 5,
            0.50,
            0.50,
            0,
            dz=2,
            dy=5
        ),

        amount=1,
        duration=10,
        scene=s
    )

    Particles3D(
         transform=Transform(
            0, 1, 0,
            0.50,
            0.50,
            0,
            dx=1,
            dz=1,
            dy=2
        ),

        amount=1,
        duration=4,
        scene=s
    )

    Particles3D(
         transform=Transform(
            10, 1, 0,
            0.50,
            0.50,
            0,
            dx=-1,
            dz=1,
            dy=2
        ),

        amount=1,
        duration=4,
        scene=s
    )

    Particles3D(
         transform=Transform(
            0, 1, 10,
            0.50,
            0.50,
            0,
            dx=1,
            dz=-1,
            dy=2
        ),

        amount=1,
        duration=4,
        scene=s
    )

    Particles3D(
         transform=Transform(
            10, 1, 10,
            0.50,
            0.50,
            0,
            dx=-1,
            dz=-1,
            dy=2
        ),

        amount=1,
        duration=4,
        scene=s
    )


engine.default_clock.Schedule.call_with_interval(gen_particles, 1 / 5)

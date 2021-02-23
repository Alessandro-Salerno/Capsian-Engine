from locals import *


def gen_square(startX, startZ, y, side):
    for x in range(startX, startX + side):
        for z in range(startZ, startZ + side):
            c = Cube(scene, Transform(x, y, z), mat)



camera  = PerspectiveCamera(Transform(0, 5, 5, 0, 0, 0, 30, -90))
controller = CharacterController()
camera.components.add(controller)
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)

scene = Scene3D(camera)
tex = Texture3D("assets/textures/glass.png")
mat = Material(texture=tex)

hud_scene = OverlayScene(camera)
counter = FPSCounter(hud_scene)

for x in range(0, 100):
        for z in range(0, 10):
            Cube(scene, Transform(x, 0, z), mat)

for y in range(0, 4):
    gen_square(12, 12, y, 12)

for y in range(0, 4):
    gen_square(12, -14, y, 12)

for y in range(0, 4):
    gen_square(34, -14, y, 12)

for y in range(0, 4):
    gen_square(34, 12, y, 12)

for y in range(0, 4):
    gen_square(56, -14, y, 12)

for y in range(0, 4):
    gen_square(56, 12, y, 12)

for y in range(0, 4):
    gen_square(78, -14, y, 12)

for y in range(0, 4):
    gen_square(78, 12, y, 12)


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


Cube(scene, Transform(13, 5, -14, 10, 50, 10), mat)
Cube(scene, Transform(35, 5, -14, 10, 50, 10), mat)
Cube(scene, Transform(57, 5, -14, 10, 50, 10), mat)
Cube(scene, Transform(79, 5, -14, 10, 50, 10), mat)

Cube(scene, Transform(13, 5, 14, 10, 50, 10), mat)
Cube(scene, Transform(35, 5, 14, 10, 50, 10), mat)
Cube(scene, Transform(57, 5, 14, 10, 50, 10), mat)
Cube(scene, Transform(79, 5, 14, 10, 50, 10), mat)

AmbientLight(Transform(18, 6, -14), Color(500, 0, 0).rgba, scene)
AmbientLight(Transform(40, 6, -14), Color(0, 500, 0).rgba, scene)
AmbientLight(Transform(61, 6, -14), Color(0, 0, 500).rgba, scene)
AmbientLight(Transform(84, 6, -14), Color(500, 500, 0).rgba, scene)

AmbientLight(Transform(18, 6, 12), Color(500, 0, 0).rgba, scene)
AmbientLight(Transform(40, 6, 12), Color(0, 500, 0).rgba, scene)
AmbientLight(Transform(61, 6, 12), Color(0, 0, 500).rgba, scene)
AmbientLight(Transform(84, 6, 12), Color(500, 500, 0).rgba, scene)

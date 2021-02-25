from Capsian import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)


scene = Scene3D(camera)
tex = Texture3D("assets/textures/glass.png")
img = Image2D("assets/textures/glass.png")
mat = Material(texture=tex)
c = Cube(scene, Transform(), mat)

hud_scene = OverlayScene(camera)
counter = FPSCounter(hud_scene)

AmbientLight(Transform(1, 1, 10), Color(0, 0, 255).rgba, scene)
AmbientLight(Transform(9, 1, 0), Color(0, 0, 255).rgba, scene)


square = Square(Transform(5, 5, 5, 5, 5, 0, 0, 0, 0), scene)
# square.flags.__setitem__("look_at_camera", True)

controller = CharacterController()
camera.components.add(controller)


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


    def on_key_pressed(self, symbol, modifiers):
        if symbol == Key.F:
            print("hello world")


camera.components.add(Keyboard())


class Mouse(MouseInputHandler):
    def on_button_held(self, buttons):
        if buttons[MouseButton.LEFT]:
            Particles2D(
                transform=Transform(
                    camera.components.transform.x,
                    camera.components.transform.y,
                    camera.components.transform.z,
                    0.25,
                    0.25,
                    0,
                    dy=-1
                ),

                amount=1,
                duration=1/3,
                scene=scene
            )


    def on_button_pressed(self, x, y, button, modifiers):
        if button == MouseButton.RIGHT:
            Particles2D(pos=camera.components.transform.position, quantity=740, direction=[3, 0.00, 0.00], scene=scene)


camera.components.add(Mouse())
pyglet.gl.glDisable(pyglet.gl.GL_CULL_FACE)

from locals import *


_lights = lights

camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)


scene = Scene(camera)
tex = Texture3D("assets/textures/glass.png")
img = Image2D("assets/textures/glass.png")
mat = Material(texture=tex)
c = Cube(material=mat, scene=scene, transform=Transform(0, 0, 0, 10, 10, 10))

hud_scene = Scene(camera, CPSN_HUD_SCENE)
counter = FPSCounter(hud_scene)

AmbientLight((1, 1,10), Color(0, 0, 255).rgba, scene)
AmbientLight((9, 1, 0), Color(0, 0, 255).rgba, scene)


square = Square(Color(255, 255, 255).rgba, (5, 5, 5), (2.5, 2.5, 5), [0, 0], scene)
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
            Particles2D(pos=camera.components.transform.position, quantity=2, direction=Direction.Vector.UP, scene=scene, lifetime=1/3)


    def on_button_pressed(self, x, y, button, modifiers):
        if button == MouseButton.RIGHT:
            Particles2D(pos=camera.components.transform.position, quantity=740, direction=[3, 0.00, 0.00], scene=scene)


camera.components.add(Mouse())
Framework.gl.glDisable(Framework.gl.GL_CULL_FACE)

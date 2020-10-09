from locals import *

_lights = lights

camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)


scene = Scene(camera)
tex = Texture3D("assets/textures/glass.png")
mat = Material(texture=tex)
c = Cube(material=mat, scene=scene, size=Size3D(10, 10, 10))

hud_scene = Scene(camera, CPSN_HUD_SCENE)
counter = FPSCounter(hud_scene)

AmbientLight(Position3D(1, 1,10), Color(0, 0, 255).rgba, scene)
AmbientLight(Position3D(9, 1, 0), Color(0, 0, 255).rgba, scene)


# square = Square(Color(255, 255, 255).rgba, Size3D(5, 5, 0), Position3D(2.5, 2.5, 5), [0, 0], scene)
# square.flags.__setitem__("look_at_camera", True)

controller = CharacterController()
camera.components.add(controller)


class Input(KeyboardInputHandler):
    def multikey(self):
        if self.pressed_key[Key.S]:
            controller.move("backwards")

        if self.pressed_key[Key.A]:
            controller.move("left")

        if self.pressed_key[Key.D]:
            controller.move("right")

        if self.pressed_key[Key.W]:
            controller.move("forwards")

        if self.pressed_key[Key.SPACE]:
            controller.move(Direction.UP)

        if self.pressed_key[Key.LSHIFT]:
            controller.move(Direction.DOWN)

Input()

# engine.main_key_listener = Input()
Framework.gl.glDisable(Framework.gl.GL_CULL_FACE)

from locals import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False)

scene = Scene(camera)
tex = Texture3D("assets/textures/glass.png")
mat = Material(texture=tex)
c = Cube(material=mat, scene=scene)

hud_scene = Scene(camera, CPSN_HUD_SCENE)
counter = FPSCounter(hud_scene)

AmbientLight(Position3D(-2, 2, -2), Color(0, 0, 255).rgba, scene)
Square(Color(255, 255, 255).rgba, Size3D(1, 1, 0), Position3D(1, 1, 1), [0, 0], scene)

controller = CharacterController()
camera.add_component(controller)


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
            controller.move("up")

        if self.pressed_key[Key.LSHIFT]:
            controller.move("down")

engine.main_key_listener = Input()

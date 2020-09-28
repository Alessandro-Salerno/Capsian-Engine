from locals import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False)

scene = Scene(camera)
tex = Texture3D("assets/textures/glass.png")
mat = Material(texture=tex)
Cube(material=mat, scene=scene)

hud_scene = Scene(camera, CPSN_HUD_SCENE)
counter = FPSCounter(hud_scene)

AmbientLight(Position3D(-2, 2, -2), Color(0, 0, 255).rgba, scene)
Square(Color(255, 255, 255).rgba, Size3D(1, 1, 0), Position3D(1, 1, 1), [0, 0], scene)


class Input(KeyboardInputHandler):
    def __init__(self):
        super().__init__()


    def get_input(self, symbol, modifiers):
        if symbol == Framework.window.key.F:
            scene.disable()

Input()

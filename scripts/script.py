from locals import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False)
# fps = FPSCounter()

s = Scene(CPSN_3D_SCENE)
texture = Texture3D(file="assets/textures/glass.png")
material = Material(texture=texture)


posizione = Position3D(0, 0, 0)
Cube(pos=posizione, scene=s, material=material)

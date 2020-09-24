from locals import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False)
fps = FPSCounter()
s = Scene(KFE_3D_SCENE)
texture = Texture3D(file="assets/textures/glass.png")
material = Material(texture=texture)

Cube(material=material, scene=s)

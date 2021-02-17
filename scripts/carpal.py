from locals import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)
# s     = Scene(camera)
scene = Scene(camera, CPSN_HUD_SCENE)

image = Image2D("assets/textures/glass.png")
sprite = DynamicSprite3D(image, [100, 100, 0], [100, 100, 0], [0, 0, 0], scene)

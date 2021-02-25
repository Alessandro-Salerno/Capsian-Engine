from Capsian import *


camera  = PerspectiveCamera()
window  = Window3D(camera=camera, vsync=False, width=1280, height=720, resizable=True)
scene   = OverlayScene(camera)

image = Image2D("assets/textures/glass.png")
sprite = DynamicSprite3D(image, Transform(100, 100, 0, 100, 100, 0), scene)
window.set_lock(False)

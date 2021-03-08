from Capsian import *


@IndependentComponent
class Setup(Script):
    def on_start(self, time) -> None:
        import scripts.data as data
        data.current_scene = Scene3D(engine.main_camera)

        overlay = OverlayScene(engine.main_camera)
        FPSCounter(overlay)

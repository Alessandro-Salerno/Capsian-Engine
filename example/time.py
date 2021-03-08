from Capsian import *


@IndependentComponent
class Timing(Script):
    def on_start(self, time) -> None:
        camera = engine.main_camera
        controller = camera.components.character_controller

        @engine.default_clock.Schedule.loop()
        def move_camera(dt: float) -> None:
            controller.move(Direction.FOWARDS)

            if round(camera.components.transform.z, 2) == 0.15:
                cm2 = PerspectiveCamera()
                window = engine.main_window
                window.set_viewport(cm2)
                window.set_mouse_lock(False)
                overlay = OverlayScene(cm2)
                SkyColor << [0, 0, 0, 0]
                Label3D(
                    "MS Gothic",
                    50,
                    "Thanks for checking this out!",
                    Color(0, 255, 0, 255).rgba,
                    Transform(
                        x=25,
                        y=window.height - 100,
                        z=0,
                        width=None,
                        height=None
                    ),
                    overlay,
                    anchor_x="left",
                    anchor_y="top"
                )

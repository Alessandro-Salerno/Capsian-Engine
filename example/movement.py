from Capsian import *


@engine.main_camera.components.component()
class Movement(KeyboardInputHandler):
    
    # Create and add character controller when started
    def on_start(self, time) -> None:
        class CC(CharacterController):
            def __init__(self):
                super().__init__()
                self.speed = 0.005

        global controller
        controller = CC()
        engine.main_camera.components.add(controller)


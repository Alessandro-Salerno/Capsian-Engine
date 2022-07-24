## ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2020 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Capsian Engine
# Copyright 2020 - 2022 Alessandro Salerno (Tzyvoski)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------


from   pyglet.gl            import *
from   pyglet.window        import key
from   capsian.log          import Log
import capsian.engine       as engine
import pyglet


class Window(pyglet.window.Window):
    """
    Fields
    ------
        mouse_lock     | The current mouse lock state                   | bool
        lighting       | Weather OpenGL lighting is on or not           | bool (Deprecated
        alive          | Weather the window is alive or not             | int
        view_port      | The viewport from which the world is drawn     | PerspectiveCamera\OrthographicCamera
        fullscreen_key | The key chosen to toggle fullscreen on and off

    Methods
    -------
        move_to_center | Moves the window to the center of the scren
        set_mouse_lock | Sets the mouse lock state to the specified value
        rotate_camera  | Rotates the viewport
        enable         | Enables a specified feature (Deprecated)
        disable        | Disables a specified feature (Deprecated)
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, camera, fullscreen_key=key.F11, *args, **kwargs):
        """
        Parameters
        ----------
            camera         | A Capsian Camera Object                         | PerspectiveCamera\OrthographicCamera
            fullscreen_key | The key that will trigger fullscreen on and off

        Additional Parameters (From Pyglet)
        -----------------------------------
            width      | The width of the window                    | int
            height     | The height of the window                   | int
            vsync      | Weather VSync is on or off                 | bool
            resizable  | Weather the window is resizable or not     | bool
            fullscreen | Weather fullscreen is on by default or not | bool
        """

        # Create window
        super().__init__(
            *args,
            **kwargs,
            screen=pyglet.canvas.Display.get_default_screen(
                pyglet.canvas.Display()
            )
        )

        # Variable declaration
        self.mouse_lock         = False
        self.fullscreen_key     = fullscreen_key

        # Others
        self.lighting           = False
        engine.main_window      = self
        self.alive              = 1

        # Looks
        self.move_to_center()

        # Checks weather the camera is compatible
        if not hasattr(camera, "init"):
            Log.critical("The specified camera is not valid")
            return

        self.view_port = camera
        camera.init()


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def move_to_center(self) -> int:
        """
        Description
        -----------
            Centers the window to the screen
        """

        x = int(self.screen.width / 2 - self.width / 2)
        y = int(self.screen.height / 2 - self.height / 2)

        self.set_location(x, y)
        return x, y


    def set_mouse_lock(self, state: bool) -> None:
        """
        Description
        -----------
            Sets the mouse lock state to the specified boolean value

        Parameters
        ----------
            state | The new value that should be assigned to "Mouse lock state" | bool
        """

        if self.alive > 0:
            self.mouse_lock = False
            self.mouse_lock = True

            self.mouse_lock = state
            self.set_exclusive_mouse(state)


    def rotate_camera(self, dx: float, dy: float) -> None:
        if not self.mouse_lock:
            return

        self.view_port.rotate(dx, dy)


    def enable(self, feature) -> None:
        mode = "enable"

        exec(compile(source=feature, filename="feature", mode="exec", optimize=1))
        Log.warning("Window.enable() is deprecated and will soon be removed")


    def disable(self, feature) -> None:
        mode = "disable"

        exec(compile(source=feature, filename="feature", mode="exec", optimize=1))
        Log.warning("Window.disable() is deprecated and will soon be removed")


########################################################################################################################


class Window3D(Window):
    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_draw(self) -> None:
        self.view_port.render(self)


    # When mouse is moved
    def on_mouse_motion(self, x: int, y: int, dx: float, dy: float) -> None:
        self.rotate_camera(dx, dy)


    # Hot fix
    def on_mouse_drag(self, x: int, y: int, dx: float, dy: float, buttons, modifiers) -> None:
        self.rotate_camera(dx, dy)


    def set_viewport(self, camera) -> None:
        """
        Description
        -----------
            Sets the rendering viewport to the specified one

        Parameters
        ----------
            camera | The new viewport | PerspectiveCamera\OrthographicCamera
        """

        if not self.alive > 0:
            return

        if not hasattr(camera, "init"):
            Log.critical("The specified camera is not valid")
            return

        camera.init()

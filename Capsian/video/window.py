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
# Copyright 2020 Alessandro Salerno (Tzyvoski)
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



from locals import Framework as pyglet
from pyglet.gl import *
from pyglet.window import key
from Capsian.values import *
from locals import Log
from locals import engine


class Window(pyglet.window.Window):
    def __init__(self, camera, fullscreen_key=key.F11, *args, **kwargs):

        # Create window
        super().__init__(*args, **kwargs, screen=pyglet.canvas.Display.get_default_screen(pyglet.canvas.Display()))

        # Variable declaration
        self.mouse_lock         = False
        self.fullscreen_key     = fullscreen_key

        # Others
        self.view_port          = camera
        self.render_static_hud  = False
        self.render_dynamic_hud = False
        self.lighting           = False
        engine.main_window      = self
        self.alive              = 1

        # Looks
        self.set_center()

        # Time
        pyglet.clock.schedule_interval(self.fixed_update, 1 / 120)

        # Test
        try:
            camera.init()
        except:
            Log.critical("The specified camera is not valid")


    # Fixed Update
    def fixed_update(self, fixed_delta_time):
        pass


    # Center the window
    def set_center(self):
        """
        Brings the window to the center of the screen

        :return: Nothing
        """

        self.set_location(round(self.screen.width / 2 - self.width / 2), round(self.screen.height / 2 - self.height / 2))


    # Set mouse lock
    def set_lock(self, state):
        """
        Switches on and off the mouse lock

        :param state:
        :return: Nothing
        """

        if self.alive > 0:
            self.mouse_lock = False
            self.mouse_lock = True

            self.mouse_lock = state
            self.set_exclusive_mouse(state)


    # Rotate camera
    def rotate_camera(self, dx, dy):
        """
        This method rotates the camera.
        This method is called by another method.
        DO NOT CALL THIS!

        :param dx: The horizontal direction in which the mouse is moving
        :param dy: The vertical direction in which the mouse is moving
        :return: Nothing
        """

        if self.mouse_lock:
            self.view_port.rotate(dx, dy)


    def on_key_press(self, symbol, modifiers):
        """
        This method gets input from the keyboard

        :param symbol: The key that's been pressed
        :param modifiers: THe modifiers used
        :return: Nothing
        """

        if self.alive > 0:
            if symbol == key.ESCAPE:
                self.close()

            if symbol == self.fullscreen_key:
                import os

                if os.name == "nt":
                    screen = pyglet.canvas.Screen(display=self.display, x=0, y=0, width=self.screen.width, height=self.screen.height, handle=None)
                    self.set_fullscreen(not self.fullscreen, screen=screen)
                else:
                    self.set_fullscreen(not self.fullscreen)

                lock = self.mouse_lock
                self.set_lock(False)
                self.set_lock(lock)

            if engine.main_key_listener is not None:
                engine.main_key_listener.single_key(symbol, modifiers)
        else:
            if symbol == key.ESCAPE or symbol == key.ENTER:
                self.close()
                pyglet.app.exit()


    # Enables a feature
    def enable(self, feature):
        mode = "enable"

        try:
            exec(compile(source=feature, filename="feature", mode="exec", optimize=1))
        except:
            Log.critical(f"'{feature}' is not valid Python code. Thus, the Window is not able to run it")


    # Disable a feature
    def disable(self, feature):
        mode = "disable"

        try:
            exec(compile(source=feature, filename="feature", mode="exec", optimize=1))
        except:
            Log.critical(f"'{feature}' is not valid Python code. Thus, the Window is not able to run it")


########################################################################################################################


class Window3D(Window):
    """
    Creates a pyglet Window (Accepts all pyglet.window.Window parameters)

    :param camera: A Capsian Camera (Camera())
    :param args: All pyglet window args
    :param kwargs: All pyglet window kwargs
    """

    def __init__(self, camera, *args, **kwargs):
        super().__init__(camera, *args, **kwargs)

        # Rendering
        self.render_distance = 50000
        self.fog_color = [0.5, 0.69, 1.0, 1]


    # Every frame
    def on_draw(self):
        """
        Calls rendering functions

        :return: Nothing
        """

        self.clear()
        self.view_port.render(self)
        pyglet.clock.tick()


    # When mouse is moved
    def on_mouse_motion(self, x, y, dx, dy):
        """
        None of the following parameters have to be specified since this method is not callable!
        to override it though, you must list all of them as parameters for your override method.
        This method is responsible for camera rotation in the 3D scene
        """

        self.rotate_camera(dx, dy)


    # Hot fix
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """
        None of the following parameters have to be specified since this method is not callable!
        to override it though, you must list all of them as parameters for your override method.
        This method is responsible for camera rotation in the 3D scene
        """

        self.rotate_camera(dx, dy)


    # When the mouse is pressed
    def on_mouse_press(self, x, y, button, modifiers):
        """
        This method is empty by default, but it can be overridden. To override it, remember to use alla listed parameters

        """

        pass


    def set_viewport(self, camera):
        """
        Sets the window's Viewport (Camera) to a specified Capsian camera object
        NOTE: It must be a class that inherits from Capsian.camera.Camera()

        :param camera: The new camera
        :return: Nothing
        """

        if self.alive > 0:
            self.view_port = camera
            camera.init()

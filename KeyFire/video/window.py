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
# KeyFire Engine
# Copyright 2019 - 2020 Alessandro Salerno (Tzyvoski)
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



import pyglet
from pyglet.gl import *
from pyglet.window import key
from KeyFire.video import graphics
from KeyFire.values import *
from locals import Log
from locals import engine


class Window(pyglet.window.Window):
    def __init__(self, camera, fullscreen_key=key.F11, *args, **kwargs):

        # Create window
        super().__init__(*args, **kwargs, screen=pyglet.canvas.Display.get_default_screen(pyglet.canvas.Display()))

        # Variable declaration
        self.mouse_lock = False
        self.fullscreen_key = fullscreen_key

        # Others
        self.view_port = camera
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.key = None
        self.render_static_hud = False
        self.render_dynamic_hud = False
        self.lighting = False
        graphics.view.__setitem__("Window", self)
        self.alive = 1
        

        # Looks
        self.set_center()

        # Time
        pyglet.clock.schedule_interval(self.fixed_update, 1 / 120)

        # Test
        try:
            camera.init()
        except:
            Log.critical("The specified camera is not valid")


    # Every frame
    def on_draw(self):

        # Window color
        glClearColor(0.5, 0.7, 1.0, 1.0)
        self.clear()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    # Fixed Update
    def fixed_update(self, fixed_delta_time):
        self.view_port.update(delta_time=fixed_delta_time, keys=self.keys)
        self.view_port.key_listener(self.keys)


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

        :param dx:
        :param dy:
        :return:
        """

        if self.mouse_lock:
            self.view_port.rotate(dx, dy)


    def on_key_press(self, symbol, modifiers):
        """
        This method gets input from the keyboard

        :param symbol:
        :param modifiers:
        :return:
        """

        if self.alive > 0:
            if symbol == key.ESCAPE:
                self.close()

            if symbol == self.fullscreen_key:
                screen = pyglet.canvas.Screen(display=self.display, x=0, y=0, width=self.screen.width, height=self.screen.height, handle=None)
                self.set_fullscreen(not self.fullscreen, screen=screen)

                lock = self.mouse_lock
                self.set_lock(False)
                self.set_lock(lock)

            if "Input" in graphics.view.keys():
                graphics.view.get("Input").get_input(symbol, modifiers)
        else:
            if symbol == key.ESCAPE or symbol == key.ENTER:
                self.close()
                pyglet.app.exit()


    def on_key_release(self, symbol, modifiers):
        if self.alive > 0:
            self.key = None


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

    :param camera: A KeyFire Camera (Camera())
    :param args:
    :param kwargs:
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

        self.view_port.render()


    # When mouse is moved
    def on_mouse_motion(self, x, y, dx, dy):
        """
        None of the following parameters have to be specified since this method is not callable!
        to override it though, you must list all of them as parameters for your override method.
        This method is responsible for camera rotation in the 3D scene

        :param x:
        :param y:
        :param dx:
        :param dy:
        :return:
        """

        self.rotate_camera(dx, dy)


    # Hot fix
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """
        None of the following parameters have to be specified since this method is not callable!
        to override it though, you must list all of them as parameters for your override method.
        This method is responsible for camera rotation in the 3D scene

        :param x:
        :param y:
        :param dx:
        :param dy:
        :return:
        """

        self.rotate_camera(dx, dy)


    # When the mouse is pressed
    def on_mouse_press(self, x, y, button, modifiers):
        """
        This method is empty by default, but it can be overridden. To override it, remember to use alla listed parameters

        :param x:
        :param y:
        :param button:
        :param modifiers:
        :return:
        """

        pass


    # Sets the render distance of the window
    def set_render_distance(self, new_render_distance):
        try:
            if new_render_distance > 0:
                self.view_port.far = new_render_distance
                Log.successful(f"Successfully changed render distance to {self.view_port.far} ")
                Log.warning("This method is deprecated and will be removed in beta 7!")
            else:
                Log.error(f"{new_render_distance} is not a valid render distance")
        except:
            Log.critical("Unable to change render distance")


    # Sets the fog color to a given one
    def set_fog_color(self, fog_color):
        """
        Sets the fog color to be the specified one

        :param fog_color: The new color of the fog (Array, [GL_R, GL_G, GL_B, GL_A]) # IN GL colors, 1 = 255 in RGBcolors
        :return:
        """

        self.fog_color = fog_color


    # Sets the clear color to be a given one
    def set_clear_color(self, clear_color):
        """
        Changes the OpenGL Clear color for the window (Default: black)

        :param clear_color: The actual color (Array, [GL_R, GL_G, GL_B, GL_A]) - in GL colors, 1 = 255 in RGB
        :return:  Nothing
        """

        if self.alive > 0:
            glClearColor(clear_color[0], clear_color[1], clear_color[2], clear_color[3])


    def set_viewport(self, camera):
        """
        Sets the window's Viewport (Camera) to a specified KeyFire camera object
        NOTE: It must be a class that inherits from KeyFire.camera.Camera()

        :param camera: The new camera
        :return: Nothing
        """

        if self.alive > 0:
            self.view_port = camera
            camera.init()
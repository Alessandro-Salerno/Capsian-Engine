# ----------------------------------------------------------------------------
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


from locals import Framework
from locals import OpenGL
import Capsian.maths.math as kmath
from locals import engine
import math


class Camera:
    def __init__(self, pos=[0, 0, 0], rot=[0, 0], fov=90, far=5000, near=0.05):
        """
        Creates a Capsian camera object in the world.
        You can create more than one, but they won't be automatically placed.
        You must create a Window3D and reference this

        :param pos: The initial position in 3D space (Array, [x, y, z])
        :param rot: The initial rotation (Array, [x, y])
        """

        # Environment
        self.pos    = list(pos)
        self.rot    = list(rot)

        # Direction vectors
        self.dy     = 0
        self.dx     = 0
        self.dz     = 0
        self.rotY   = 0
        self.rotX   = 0

        # Other vars
        self.sens   = 0.1
        self.s      = 0
        self.keys   = None

        # Rendering
        self.fov    = fov
        self.far    = int(far)
        self.near   = float(near)
        self.scenes = []

        self.keys   = [
            Framework.window.key.W,
            Framework.window.key.A,
            Framework.window.key.S,
            Framework.window.key.D,
            Framework.window.key.LSHIFT,
            Framework.window.key.SPACE
        ]

        self.args   = {
            self.keys[0]: "forwards",
            self.keys[1]: "left",
            self.keys[2]: "backwards",
            self.keys[3]: "right",
            self.keys[4]: "down",
            self.keys[5]: "up"
        }


    # Update every frame
    def update(self, delta_time, keys):
        """
        This method allows camera movement and calls the input method

        :param delta_time: 1 tick (1/120 sec)
        :param keys: KeyInputHandler (Given from window)
        :return: Nothing
        """

        self.s    = delta_time * 50
        self.rotY = -self.rot[1] / 180 * math.pi

        self.dx   = self.s * math.sin(self.rotY)
        self.dz   = self.s * math.cos(self.rotY)

        self.keys = keys


    def get_field_of_view(self):
        """
        The current field of view of the camera

        :return: Float/Int Field of View (Default: 90)
        """

        return self.fov


    def set_field_of_view(self, fov):
        """

        Sets the field of view of the camera

        :param fov: The new field of view
        :return: Nothing
        """

        self.fov = fov


########################################################################################################################


class PerspectiveCamera(Camera):
    def __init__(self, pos=[0, 0, 0], rot=[0, 0], fov=90, far=5000, near=0.05):
        super().__init__(pos, rot, fov, far, near)

        self.hud_scenes = []


    def init(self):
        engine.main_camera = self

        OpenGL.glEnable(OpenGL.GL_DEPTH_TEST)
        OpenGL.glEnable(OpenGL.GL_NORMALIZE)
        OpenGL.glEnable(OpenGL.GL_CULL_FACE)
        OpenGL.glCullFace(OpenGL.GL_BACK)

        engine.main_window.set_lock(True)
        engine.main_window.set_caption("Capsian 1.0 Window - 3D Mode")


    def render(self, window):
        # Set all OpenGL parameters
        OpenGL.glClear(OpenGL.GL_COLOR_BUFFER_BIT | OpenGL.GL_DEPTH_BUFFER_BIT)

        if window.lighting: OpenGL.glEnable(OpenGL.GL_LIGHTING)

        OpenGL.glMatrixMode(OpenGL.GL_PROJECTION)
        OpenGL.glLoadIdentity()

        OpenGL.gluPerspective(self.fov,
                              window.width / window.height,
                              self.near,
                              self.far)

        OpenGL.glMatrixMode(OpenGL.GL_MODELVIEW)
        OpenGL.glLoadIdentity()

        OpenGL.glPushMatrix()
        OpenGL.glRotatef(-self.rot[0], 1, 0, 0)
        OpenGL.glRotatef(-self.rot[1], 0, 1, 0)
        OpenGL.glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

        
        # Render 3D Scene
        for scene in self.scenes:
            scene.batch.draw()
            
            for light in scene.lights:
                light.render()

            for object2D in scene.objects2D:
                object2D.draw()

        OpenGL.glPopMatrix()

        # Render the HUD in the scene
        if window.render_static_hud:
            OpenGL.glDisable(OpenGL.GL_LIGHTING)
            width, height = window.get_size()
            viewport = window.get_viewport_size()
            OpenGL.glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
            OpenGL.glMatrixMode(OpenGL.GL_PROJECTION)
            OpenGL.glLoadIdentity()
            OpenGL.glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
            OpenGL.glMatrixMode(OpenGL.GL_MODELVIEW)
            OpenGL.glLoadIdentity()
            
            # Render HUD 
            for scene in self.hud_scenes:
                scene.hud_batch.draw()

        if window.render_dynamic_hud:
            OpenGL.glDisable(OpenGL.GL_LIGHTING)
            width, height = window.get_size()
            viewport = window.get_viewport_size()
            OpenGL.glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
            OpenGL.glMatrixMode(OpenGL.GL_PROJECTION)
            OpenGL.glLoadIdentity()
            OpenGL.glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
            OpenGL.glMatrixMode(OpenGL.GL_MODELVIEW)
            OpenGL.glLoadIdentity()
            
            for scene in self.hud_scenes:
                for hud in scene.dynamic_hud:
                    hud.draw()


    # Handles mouse rotation
    def rotate(self, dx, dy):
        """
        This method rotates the camera. IT's called by Window3D.rotate_camera()

        :param dx: The direction the mouse is heading towards on the x axis
        :param dy: The direction the mouse is heading towards on the y axis
        :return: Nothing
        """

        dx /= 8
        dy /= 8

        self.rot[0] += dy
        self.rot[1] -= dx

        self.rot[0]  = kmath.clamp(90, -90, self.rot[0])


    # Get input for movement
    def key_listener(self, handler):
        """
        This method listens to input from your keyboard

        :param handler: The key state handler given by the main window
        :return: Nothing
        """

        for k in self.keys:
            if handler[k] and k in self.args.keys():
                self.move(self.args[k])
            else:
                continue


    # Move camera
    def move(self, direction):
        """
        This method actually moves the camera, it's called by Camera.update()

        :param direction: The direction in which the camera should move (String)
        :return:
        """

        if direction    == "forwards":
            self.pos[0] += self.dx * self.sens * engine.main_window.alive
            self.pos[2] -= self.dz * self.sens * engine.main_window.alive

        if direction    == "backwards":
            self.pos[0] -= self.dx * self.sens * engine.main_window.alive
            self.pos[2] += self.dz * self.sens * engine.main_window.alive

        if direction    == "right":
            self.pos[0] += self.dz * self.sens * engine.main_window.alive
            self.pos[2] += self.dx * self.sens * engine.main_window.alive

        if direction    == "left":
            self.pos[0] -= self.dz * self.sens * engine.main_window.alive
            self.pos[2] -= self.dx * self.sens * engine.main_window.alive

        if direction    == "down":
            self.pos[1] -= self.s / 10 * engine.main_window.alive

        if direction    == "up":
            self.pos[1] += self.s / 10 * engine.main_window.alive


    # Repr dunderscore method
    def __repr__(self):
        return "PerspectiveCamera"


########################################################################################################################


class OrthographicCamera(Camera):
    def __init__(self, pos=[0, 0, 0], rot=[0, 0], fov=90):
        super().__init__(pos=pos, rot=rot, fov=fov)


    def init(self):
        engine.main_camera = self

        OpenGL.glDisable(OpenGL.GL_DEPTH_TEST)
        engine.main_window.set_lock(False)
        engine.main_window.set_caption("Capsian 1.0 Window - GUI Mode")


    def render(self, window):
        # Render the 2D scene
        OpenGL.glDisable(OpenGL.GL_LIGHTING)
        width, height = window.get_size()
        viewport = window.get_viewport_size()
        OpenGL.glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        OpenGL.glMatrixMode(OpenGL.GL_PROJECTION)
        OpenGL.glLoadIdentity()
        OpenGL.glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        OpenGL.glMatrixMode(OpenGL.GL_MODELVIEW)
        OpenGL.glLoadIdentity()
        
        for scene in self.scenes:
            scene.batch.draw()

            for gui in scene.dynamic_gui:
                gui.draw()


    def rotate(self, dx, dy):
        pass


    def key_listener(self, handler):
        pass


    # Repr dunderscore method
    def __repr__(self):
        return "OrthographicCamera"
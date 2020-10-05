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
import Capsian.maths.math as kmath
from locals import engine
from Capsian.entities.entity import Entity
import math


class Camera(Entity):
    def __init__(self, pos=[0, 0, 0], rot=[0, 0], fov=90, far=5000, near=0.05):
        """
        Creates a Capsian camera object in the world.
        You can create more than one, but they won't be automatically placed.
        You must create a Window3D and reference this

        :param pos: The initial position in 3D space (Array, [x, y, z])
        :param rot: The initial rotation (Array, [x, y])
        """

        # Environment
        super().__init__(pos=pos, rot=rot)

        # Direction vectors
        self.dx       = 0
        self.dy       = 0
        self.dz       = 0
        self.rotY     = 0
        self.rotX     = 0
        self.mouse_dx = 0
        self.mouse_dy = 0

        # Other vars
        self.keys     = None

        # Rendering
        self._fov     = fov
        self.far      = int(far)
        self.near     = float(near)
        self.scenes   = []


    @property
    def fov(self):
        """
        The current field of view of the camera

        :return: Float/Int Field of View (Default: 90)
        """

        return self._fov


    def set_fov(self, fov):
        """
        Sets the field of view of the camera

        :param fov: The new field of view
        :return: Nothing
        """

        self._fov = fov


########################################################################################################################


class PerspectiveCamera(Camera):
    def __init__(self, pos=[0, 0, 0], rot=[0, 0], fov=90, far=5000, near=0.05):
        super().__init__(pos, rot, fov, far, near)
        self.hud_scenes = []


    def init(self):
        engine.main_camera = self

        Framework.gl.glEnable(Framework.gl.GL_DEPTH_TEST)
        Framework.gl.glEnable(Framework.gl.GL_NORMALIZE)
        Framework.gl.glEnable(Framework.gl.GL_CULL_FACE)
        Framework.gl.glCullFace(Framework.gl.GL_BACK)
        Framework.gl.glEnable(Framework.gl.GL_BLEND)
        Framework.gl.glBlendFunc(Framework.gl.GL_SRC_ALPHA, Framework.gl.GL_ONE_MINUS_SRC_ALPHA)

        engine.main_window.set_lock(True)
        engine.main_window.set_caption("Capsian 1.0 Window - 3D Mode")


    def render(self, window):
        # Set all OpenGL parameters
        Framework.gl.glClear(Framework.gl.GL_COLOR_BUFFER_BIT | Framework.gl.GL_DEPTH_BUFFER_BIT)

        if window.lighting: Framework.gl.glEnable(Framework.gl.GL_LIGHTING)

        Framework.gl.glMatrixMode(Framework.gl.GL_PROJECTION)
        Framework.gl.glLoadIdentity()

        Framework.gl.gluPerspective(self.fov,
                              window.width / window.height,
                              self.near,
                              self.far)

        Framework.gl.glMatrixMode(Framework.gl.GL_MODELVIEW)
        Framework.gl.glLoadIdentity()

        Framework.gl.glPushMatrix()
        Framework.gl.glRotatef(-self.rot[0], 1, 0, 0)
        Framework.gl.glRotatef(-self.rot[1], 0, 1, 0)
        Framework.gl.glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

        
        # Render 3D Scene
        for scene in self.scenes:
            for light in scene.lights:
                light.render()

            for object2D in scene.objects2D:
                object2D.draw()

            scene.batch.draw()

        Framework.gl.glPopMatrix()

        Framework.gl.glDisable(Framework.gl.GL_LIGHTING)
        width, height = window.get_size()
        viewport = window.get_viewport_size()
        Framework.gl.glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        Framework.gl.glMatrixMode(Framework.gl.GL_PROJECTION)
        Framework.gl.glLoadIdentity()
        Framework.gl.glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        Framework.gl.glMatrixMode(Framework.gl.GL_MODELVIEW)
        Framework.gl.glLoadIdentity()
            
        # Render HUD 
        for scene in self.hud_scenes:
            scene.hud_batch.draw()

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

        self.mouse_dx = dx / 8
        self.mouse_dy = dy / 8


    # Repr dunderscore method
    def __repr__(self):
        return "PerspectiveCamera"


########################################################################################################################


class OrthographicCamera(Camera):
    def __init__(self, pos=[0, 0, 0], rot=[0, 0], fov=90):
        super().__init__(pos=pos, rot=rot, fov=fov)


    def init(self):
        engine.main_camera = self

        Framework.gl.glDisable(Framework.gl.GL_DEPTH_TEST)
        engine.main_window.set_lock(False)
        engine.main_window.set_caption("Capsian 1.0 Window - GUI Mode")


    def render(self, window):
        # Render the 2D scene
        Framework.gl.glDisable(Framework.gl.GL_LIGHTING)
        width, height = window.get_size()
        viewport = window.get_viewport_size()
        Framework.gl.glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        Framework.gl.glMatrixMode(Framework.gl.GL_PROJECTION)
        Framework.gl.glLoadIdentity()
        Framework.gl.glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        Framework.gl.glMatrixMode(Framework.gl.GL_MODELVIEW)
        Framework.gl.glLoadIdentity()
        
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

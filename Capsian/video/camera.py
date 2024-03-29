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


from   Capsian.components.transform import Transform
from   Capsian.entities.entity      import Entity
from   Capsian.video.window         import Window3D
import Capsian.maths.math           as     kmath
import Capsian.engine               as     engine
import math
import pyglet


class Camera(Entity):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=Transform(), fov=90, far=5000, near=0.05):
        """
        Parameters
        ----------
            transform | A Capsian transform component | Transform
            fov       | The field of view             | int < 180
            far       | The furthest point in view    | float
            near      | The nearest point in view     | float
        """

        super().__init__(
            transform,
            active=True
        )

        # Direction vectors
        self.dx         = 0
        self.dy         = 0
        self.dz         = 0
        self.rotY       = 0
        self.rotX       = 0
        self.mouse_dx   = 0
        self.mouse_dy   = 0

        # Rendering
        self.fov        = fov
        self.far        = int(far)
        self.near       = float(near)
        self.scenes     = []
        self.hud_scenes = []


########################################################################################################################


class PerspectiveCamera(Camera):
    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def init(self):
        engine.main_camera = self
        engine.main_window.view_port = self

        pyglet.gl.glEnable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glEnable(pyglet.gl.GL_NORMALIZE)
        pyglet.gl.glEnable(pyglet.gl.GL_CULL_FACE)
        pyglet.gl.glCullFace(pyglet.gl.GL_BACK)
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        engine.main_window.set_mouse_lock(True)
        engine.main_window.set_caption("Capsian 1.0 Window - 3D Mode")


    def render(self, window: Window3D) -> None:
        # Set all OpenGL parameters
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT)

        if window.lighting: pyglet.gl.glEnable(pyglet.gl.GL_LIGHTING)

        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()

        if window.width < 1 or window.height < 1:
            return

        pyglet.gl.gluPerspective(
            self.fov,
            window.width / window.height,
            self.near,
            self.far
        )

        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glLoadIdentity()

        pyglet.gl.glPushMatrix()

        pyglet.gl.glRotatef(
            -self.components.transform.rotX,
            1, 0, 0
        )

        pyglet.gl.glRotatef(
            -self.components.transform.rotY,
            0, 1, 0
        )

        pyglet.gl.glTranslatef(
            -self.components.transform.x,
            -self.components.transform.y,
            -self.components.transform.z
        )

        
        # Render 3D Scene
        for scene in self.scenes:
            for element in scene.drawable:
                element.draw()

            scene.batch.draw()

        pyglet.gl.glPopMatrix()
        pyglet.gl.glDisable(pyglet.gl.GL_LIGHTING)
        
        width, height = window.get_size()
        viewport      = window.get_viewport_size()

        pyglet.gl.glViewport(
            0,
            0,
            max(
                1,
                viewport[0]
            ),
            max(
                1,
                viewport[1]
            )
        )

        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()

        pyglet.gl.glOrtho(
            0,
            max(
                1,
                width
            ),
            0,
            max(
                1,
                height
            ),
            -1,
            1
        )

        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glLoadIdentity()
        
        # Render HUD 
        for scene in self.hud_scenes:
            scene.hud_batch.draw()

            for hud in scene.dynamic_hud:
                hud.draw()


    # Handles mouse rotation
    def rotate(self, dx: float, dy: float):
        """
        This method rotates the camera. IT's called by Window3D.rotate_camera()

        :param dx: The direction the mouse is heading towards on the x axis
        :param dy: The direction the mouse is heading towards on the y axis
        :return: None
        """

        self.mouse_dx = dx / 8
        self.mouse_dy = dy / 8

        if self.components.character_controller is not None:
            self.components.character_controller.rotate()


class OrthographicCamera(Camera):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def init(self):
        engine.main_camera = self
        engine.main_window.view_port = self

        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)
        engine.main_window.set_mouse_lock(False)
        engine.main_window.set_caption("Capsian 1.0 Window - GUI Mode")


    def render(self, window: Window3D) -> None:
        # Render the 2D scene
        pyglet.gl.glDisable(pyglet.gl.GL_LIGHTING)
        
        width, height = window.get_size()
        viewport     = window.get_viewport_size()

        pyglet.gl.glViewport(
            0,
            0,

            max(
                1,
                viewport[0]
            ),
            
            max(
                1,
                viewport[1]
            )
        )

        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()

        pyglet.gl.glOrtho(
            0,

            max(
                1,
                width
            ),

            0,

            max(
                1,
                height
            ),

            -1,
            1
        )

        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glLoadIdentity()
        
        for scene in self.scenes:
            scene.batch.draw()

            for gui in scene.dynamic_gui:
                gui.draw()


    def rotate(self, dx: float, dy: float) -> None:
        pass

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
# Copyright 2020 - 2021 Alessandro Salerno (Tzyvoski)
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



from Capsian.entities.entity      import Entity
from Capsian.components.transform import Transform
import Capsian.engine             as engine
import pyglet


class Square(Entity):
    """
    Squares are strictly correlated to particles.
    Particles, in fact, are just groups of squares that can move...
    A Capsian Square is a 2D quad in 3D space
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=None, scene=None, active=False):
        """
        Creates a square in the world

        :param transform: Tramsform object that holds positioning data (Transform())
        :param scene: Capsian Scene object (Scene3D()/Scene2D()/PlaceholderScene)
        """

        super().__init__(
            transform=transform,
            scene=scene,
            active=active
        )

        x                = transform.size[0] / 2
        y                = transform.size[1] / 2
        z                = transform.size[2] / 2

        self.currentX    = x
        self.currentY    = y

        self.vertex_list = pyglet.graphics.vertex_list(
            4,
            (
                'v3f',
                [
                    0, 0, 0,
                    transform.size[0], 0, 0,
                    transform.size[0], transform.size[1], 0,
                    0, transform.size[1], 0
                ]
            ),

            (
                't3f',
                [
                    0, 0, 0,
                    1, 0, 0,
                    1, 1, 0,
                    0, 1, 0
                ]
            )
        )

        scene.objects2D.append(self)
        scene.drawable.append(self)


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    # Draw OpenGL quad (Old OpenGL)
    def draw(self):
        pyglet.gl.glPushMatrix()

        pyglet.gl.glTranslatef(
            self.components.transform.x,
            self.components.transform.y,
            self.components.transform.z
        )

        self.vertex_list.draw(pyglet.gl.GL_QUADS)
        pyglet.gl.glPopMatrix()


    # Delte self
    def delete(self):
        if self in self.scene.objects2D:
            self.scene.objects2D.remove(self)
            self.scene.drawable.remove(self)
            
        del self


class TexturedSquare(Square):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, texture, transform, scene):
        self.texture = texture.get_texture()

        super().__init__(
            transform,
            scene,
            False
        )


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    # Draw OpenGL quad (Old OpenGL)
    def draw(self):
        pyglet.gl.glPushMatrix()

        pyglet.gl.glTranslatef(
            self.components.transform.x,
            self.components.transform.y,
            self.components.transform.z
        )

        pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
        pyglet.gl.glBindTexture(pyglet.gl.GL_TEXTURE_2D, self.texture.id)

        self.vertex_list.draw(pyglet.gl.GL_QUADS)
        pyglet.gl.glDisable(pyglet.gl.GL_TEXTURE_2D)

        pyglet.gl.glPopMatrix()


class RotatingSquare(Square):
    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    # Draw OpenGL quad (Old OpenGL)
    def draw(self):
        pyglet.gl.glPushMatrix()

        pyglet.gl.glTranslatef(
            self.components.transform.x,
            self.components.transform.y,
            self.components.transform.z
        )

        pyglet.gl.glRotatef(
            engine.main_camera.components.transform.rotX,

            -1,
            0,
            0
        )

        pyglet.gl.glRotatef(
            engine.main_camera.components.transform.rotY,

            0,
            1,
            0
        )

        self.vertex_list.draw(pyglet.gl.GL_QUADS)
        pyglet.gl.glPopMatrix()

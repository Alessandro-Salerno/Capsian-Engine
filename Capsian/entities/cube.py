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


from   Capsian.entities.entity      import Entity
from   Capsian.components.transform import Transform
import pyglet


class Cube(Entity):
    """
    A Cube object is 3D Cube.
    This object uses Batched rendering for high performance and Capsian materials for texturing.

    Fields
    ------
        next_pos | A list of adjacent positions | list
        texture  | The cube's texture           | texture

    Methods
    -------
        _add_block | Adds the cube to the scene
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=Transform(), scene=None, material=None):
        """
        Parameters
        ----------
            transform | A Capsian Transform Component | Transform
            scene     | A Capsian Scene Object        | Scene3D
            material  | A Capsian Material Object     | Material
        """

        super().__init__(
            scene=scene,
            transform=transform
        )

        self.texture  = material.texture
        self._add_block(
            transform.x,
            transform.y,
            transform.z
        )


    # -------------------------
    #
    #       PRIVATE METHODS
    #
    # -------------------------

    # Add faces to batch
    def _add_block(self, x: float, y: float, z: float) -> None:
        """
        Definition
        ----------
            Adds the cube to the scene's world

        Parameters
        ----------
            x | The cube's X position | float
            y | The cube's Y position | float
            z | The cube's Z position | float
        """

        X, Y, Z    = x + self.components.transform.width, \
                     y + self.components.transform.height, \
                     z + self.components.transform.depth

        tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

        # Back
        self.scene.batch.add(
            4,
            pyglet.gl.GL_QUADS,
            self.texture,
            (
                'v3f',
                (
                    X, y, z,
                    x, y, z,
                    x, Y, z,
                    X, Y, z
                )
            ),
            tex_coords
        )

        # Front
        self.scene.batch.add(
            4,
            pyglet.gl.GL_QUADS,
            self.texture,
            (
                'v3f',
                (
                    x, y, Z,
                    X, y, Z,
                    X, Y, Z,
                    x, Y, Z
                )
            ),
            tex_coords
        )

        # Left
        self.scene.batch.add(
            4,
            pyglet.gl.GL_QUADS,
            self.texture,
            (
                'v3f',
                (
                    x, y, z,
                    x, y, Z,
                    x, Y, Z,
                    x, Y, z
                )
            ),
            tex_coords
        )

        # Right
        self.scene.batch.add(
            4,
            pyglet.gl.GL_QUADS,
            self.texture,
            (
                'v3f',
                (
                    X, y, Z,
                    X, y, z,
                    X, Y, z,
                    X, Y, Z
                )
            ),
            tex_coords
        )

        # Bottom
        self.scene.batch.add(
            4,
            pyglet.gl.GL_QUADS,
            self.texture,
            (
                'v3f',
                (
                    x, y, z,
                    X, y, z,
                    X, y, Z,
                    x, y, Z
                )
            ),
            tex_coords
        )

        # Top
        self.scene.batch.add(
            4,
            pyglet.gl.GL_QUADS,
            self.texture,
            (
                'v3f',
                (
                    x, Y, Z,
                    X, Y, Z,
                    X, Y, z,
                    x, Y, z
                )
            ),
            tex_coords
        )

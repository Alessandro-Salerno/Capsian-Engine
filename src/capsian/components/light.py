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


from   capsian.log                  import Log
from   capsian.components.component import Component
import pyglet


class Light(Component):
    """
    A Capsian Light Component allows you to add lights to entities.
    It currently uses Old OpenGL, so you can't use more than 8 lights in your game!

    Fields
    ------
        type      | The light's type
        intensity | The light's oclor and intensity | list [R, G, B, A]
        light     | The OpenGL light (Ex: GL_LIGHT0)

    Properties
    ----------
        parent | The light component's parent object

    Methods
    -------
        draw | Renders the light object
    """

    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, gl_light, color: list):
        """
        Parameters
        ----------
            gl_light | The OpenGL Light value                                  | GL_AMBIENT\GL_DIFFUSE\GL_SPECULAR
            color    | A list of four values describing the color of the light | list [R, G, B, A]
        """

        from capsian.values import lights

        super().__init__()

        self.type          = gl_light
        self.intensity     = list(color)

        if not len(lights) > 0:
            self.light = pyglet.gl.GL_LIGHT0
            Log.error("Unable to create light: All 8 light slots available are taken!")
            return

        self.light = lights[0]
        lights.pop(0)


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_ready(self, time) -> None:
        pyglet.gl.glEnable(self.light)
        self.parent.scene.lights.append(self)
        self.parent.scene.drawable.append(self)


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    # Draw the light
    def draw(self) -> None:
        """
        Description
        -----------
            This method is responsible for rendering the light in the scene.
            This method takes no paramters and should not ba called outside of the internal rendering functions
        """

        pyglet.gl.glLightfv(
            self.light,
            pyglet.gl.GL_POSITION,
            (pyglet.gl.GLfloat * 4) (
                self.parent.components.transform.x,
                self.parent.components.transform.y,
                self.parent.components.transform.z,
                1
            )
        )

        pyglet.gl.glLightfv(
            self.light,
            self.type,
            (pyglet.gl.GLfloat * 3) (
                self.intensity[0],
                self.intensity[1],
                self.intensity[2]
            )
        )

        pyglet.gl.glLightfv(
            self.light,
            pyglet.gl.GL_QUADRATIC_ATTENUATION,
            (pyglet.gl.GLfloat * 1) (1)
        )


########################################################################################################################


class AmbientLight(Light):
    def __init__(self, color: list):
        """
        Parameters
        ----------
            color | A list of four values describing the color of the light | list [R, G, B, A]
        """

        from capsian.values import CPSN_AMBIENT_LIGHT

        super().__init__(
            CPSN_AMBIENT_LIGHT,
            color
        )


class DiffusedLight(Light):
    def __init__(self, color: list):
        """
        Parameters
        ----------
            color | A list of four values describing the color of the light | list [R, G, B, A]
        """

        from capsian.values import CPSN_DIFFUSE_LIGHT

        super().__init__(
            CPSN_AMBIENT_LIGHT,
            color
        )


class SpecularLight(Light):
    def __init__(self, color: list):
        """
        Parameters
        ----------
            color | A list of four values describing the color of the light | list [R, G, B, A]
        """

        from capsian.values import CPSN_SPECULAR_LIGHT

        super().__init__(
            CPSN_SPECULAR_LIGHT,
            color
        )

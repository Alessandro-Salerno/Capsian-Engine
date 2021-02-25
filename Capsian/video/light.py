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


from Capsian.log import Log
import pyglet


class Light3D:
    def __init__(self, light_type, transform, color, scene):
        """
        Creates an OpenGL Light in a given position with a given intensity.
        You can specify the type of light using this!

        :param light_type: The type of light (such as GL_AMBIENT)
        :param pos: The position in 3D space (Array, [x, y, z])
        :param color: The color and intensity of the light (Array, [R, G, B]) - You can set any of value to whatever you want (Example: R = 3435)
        """

        from Capsian.values import lights

        self.type          = light_type
        self.pos           = transform.position
        self.intensity     = color
        self.scene         = scene

        try:
            if not len(lights) > 0:
                self.light = pyglet.gl.GL_LIGHT0
                Log.critical(f"The Light3D object at world position [{pos[0]}, {pos[1]}, {pos[2]} could not be created as there is no OpenGL light available. You can have a maximum of 8 lights in your program for now. This will be fixed in a later version though!")
                raise Exception()

            self.light = lights[0]
            lights.pop(0)
        except:
            Log.critical("Unable to create light. You can only have 8 lights in a given scene (GL_LIGHT0 - GL_LIGHT7). Check if you tried to add more than that and if you are, remove some lights or try finding creative ways to render them separatelly")

        pyglet.gl.glEnable(self.light)
        scene.lights.append(self)
        scene.drawable.append(self)


    # Draw the light
    def draw(self):
        """
        Draws the light.
        This method is called by graphics.draw() and MUST NOT be called by other cde

        :return: None
        """

        pyglet.gl.glLightfv(self.light, pyglet.gl.GL_POSITION, (pyglet.gl.GLfloat * 4)(self.pos[0], self.pos[1], self.pos[2], 1))
        pyglet.gl.glLightfv(self.light, self.type, (pyglet.gl.GLfloat * 3)(self.intensity[0], self.intensity[1], self.intensity[2]))
        pyglet.gl.glLightfv(self.light, pyglet.gl.GL_QUADRATIC_ATTENUATION, (pyglet.gl.GLfloat * 1)(1))


########################################################################################################################


class AmbientLight(Light3D):
    def __init__(self, transform, color, scene):
        """
        Creates an OpenGL Ambient light.
        You can't specify a light type in this!

        :param light_type: The type of light (such as GL_AMBIENT)
        :param pos: The position in 3D space (Array, [x, y, z])
        :param color: The color and intensity of the light (Array, [R, G, B]) - You can set any of value to whatever you want (Example: R = 3435)
        """

        from Capsian.values import CPSN_AMBIENT_LIGHT
        super().__init__(CPSN_AMBIENT_LIGHT, transform, color, scene)

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



from locals import *


class Square(Entity):
    """
    Squares are strictly correlated to particles.
    Particles, in fact, are just groups of squares that can move...
    A Capsian Square is a 2D quad in 3D space

    """

    def __init__(self, color, size, pos, rot, scene):
        """
        Creates a square in the world

        :param color: Nothing
        :param size: Size of the square (Array, [length, height])
        :param pos: The position of the square in 3D space (Array, [x, y, z])
        :param rot: The rotation of the square (Array, [rx, ry, rz])
        """

        super().__init__(size=size, pos=pos, rot=rot, scene=scene)
        x                = size[0] / 2
        y                = size[1] / 2
        z                = size[2] / 2

        self.currentX    = x
        self.currentY    = y

        self.vertex_list = Framework.graphics.vertex_list(4,
                                                          ('v3f', [0, 0, 0, self.size[0], 0, 0, self.size[0], self.size[1], 0, 0, self.size[1], 0]),
                                                          ('t3f', [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0])
                                                          )

        self.color       = color
        self.visible     = True
        self.scene       = scene

        self.flags       = {
            "look_at_camera": False,
        }

        self.id          = len(scene.objects2D)
        scene.objects2D.insert(self.id, self)


    # Draw OpenGL quad (Old OpenGL)
    def draw(self):
        """
        Draws a given square

        :return: Nothing
        """

        Framework.gl.glPushMatrix()
        Framework.gl.glTranslatef(self.pos[0], self.pos[1], self.pos[2])

        if self.check_flag("look_at_camera"):
            self.look_at_camera()

        self.vertex_list.draw(Framework.gl.GL_QUADS)
        Framework.gl.glPopMatrix()


    # Stop rendering
    def stop_rendering(self):
        """
        This method will tell the engine to stop rendering a given square

        :return: Nothing
        """

        self.visible = False


    # Look at the player
    def look_at_camera(self):
        """
        This method rotates a square towards the camera

        :return: Nothing
        """

        Framework.gl.glRotatef(
            engine.main_camera.rot[1],

            0,
            1,
            0
        )

        Framework.gl.glRotatef(
            engine.main_camera.rot[0],

            1,
            0,
            0
        )


    # Check flags
    def check_flag(self, flag):
        """
        This method checks a given flag to see if it's on or off

        :param flag: The flag that should be checked (String)
        :return: Value of the flag (Boolean, String, Int... Depends on the flag)
        """

        if flag in self.flags:
            return self.flags[flag]
        else:
            Log.critical(f"No flag named '{flag}' was found. Check the documentation or add the flag in the dictionary yourself")


    # Set flags
    def set_flag(self, flag, state):
        """
        This method sets the given flag on or off

        :param flag: The flag you want to change (String)
        :param state: The state you want to set it at (Boolean)
        :return: Nothing
        """

        if flag in self.flags:
            self.flags.__setitem__(flag, state)
        else:
            Log.critical(f"No flag named '{flag}' was found. Check the documentation or add the flag in the dictionary yourself")


    # Returns boolean
    def is_visible(self):
        """
        This method tells you if a given square is visible or not

        :return: Boolean
        """

        return self.visible


    # Returns int pointer
    def get_id(self):
        """
        This method tells you the id of a given square

        :return: Int
        """

        return self.id


    # Delte self
    def delete(self):
        """
        This method removes a square from the stack graphics.objects2D

        :return: Nothing
        """

        self.scene.objects2D.remove(self)
        self.__del__()


    def __del__(self):
        del self


class TexturedSquare(Square):
    def __init__(self, texture, size, pos, rot):
        super().__init__([255, 255, 255, 255], size, pos, rot)

        self.texture = texture.get_texture()
        graphics.dynamic_hud.append(self)


    def quad(self):
        pass


    def draw(self):
        """
        Draws a given square

        :return: Nothing
        """

        Framework.gl.glPushMatrix()

        Framework.gl.glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        Framework.gl.glEnable(Framework.gl.GL_TEXTURE_2D)
        Framework.gl.glBindTexture(Framework.gl.GL_TEXTURE_2D, self.texture.id)

        if self.check_flag("look_at_camera"):
            self.look_at_camera()

        self.vertex_list.draw(Framework.gl.GL_QUADS)
        Framework.gl.glDisable(Framework.gl.GL_TEXTURE_2D)

        Framework.gl.glPopMatrix()

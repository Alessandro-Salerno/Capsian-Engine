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


def TextureMode(filter1, filter2, algorithm):
    """
    Converts a series of values into a Texture Compatible OpenGL Texture Mode.
    The default Texture Mode is specified by CPSN_DEFAULT_TEXTURE_MODE and is applied to all textures by default.
    This mode is great for pixel art, but may be out of touch for more defined textures.

    :param filter1: The first filter (Default: pyglet.gl.GL_TEXTURE_MIN_FILTER)
    :param filter2: The second filter (Default: pyglet.gl.GL_TEXTURE_MAG_FILTER)
    :param algorithm: The scaling algorithm used by OpenGL (Default: pyglet.gl.GL_NEAREST)

    :return: Array [filter1, filter2, algorithm]
    """

    return [filter1, filter2, algorithm]


class Color:
    """
    A color object is not always useful.
    It's designed to help you to convert different color types (Such as RGB to Float)

    """

    def __init__(self, r=255, g=255, b=255, a=255):
        self.rgba = [r, g, b, a]


    def convert_to(self, to):
        methods = {
            "rgb": self._convert_to_byte_color,
            "glf": self._convert_to_gl_float_color,
        }

        if to in methods.keys():
            methods[to]()
        else:
            from Capsian import Log
            Log.error(f"'{to}' is not a valid color type")


    @property
    def _convert_to_gl_float_color(self):
        """
        Converts RGB/RGBA to OpenGL float color

        :return: Array [FloatR, FloatG, FloatB, FloatA]
        """

        gl_colors = [0, 0, 0, 0]

        for i in range(0, len(self.rgba)):
            gl_colors[i] = self.rgba[i] / 255

        return gl_colors


    @property
    def _convert_to_byte_color(self):
        """
        Converts OpenGL float color into RGBA

        :return: Array [R, G, B, A]
        """

        byte_colors = [0, 0, 0, 0]

        for i in range(0, len(self.rgba)):
            byte_colors[i] = self.rgba[i] * 255

        return byte_colors

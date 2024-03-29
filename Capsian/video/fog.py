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


import pyglet


class Fog:
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, color: list, start: float, end: float):
        self.color = color
        self.start = float(start)
        self.end   = float(end)

        self.enable(color, start, end)


    # -------------------------
    #
    #       STATIC METHODS
    #
    # -------------------------

    @staticmethod
    def enable(color: list, start: float, end: float) -> None:
        pyglet.gl.glEnable(pyglet.gl.GL_FOG)
        
        pyglet.gl.glFogfv(
            pyglet.gl.GL_FOG_COLOR,
            (pyglet.gl.GLfloat * 4) (
                color[0],
                color[1],
                color[2],
                color[3]
            )
        )

        pyglet.gl.glHint(
            pyglet.gl.GL_FOG_HINT,
            pyglet.gl.GL_NICEST
        )

        pyglet.gl.glFogf(
            pyglet.gl.GL_FOG_MODE,
            pyglet.gl.GL_LINEAR
        )

        pyglet.gl.glFogf(
            pyglet.gl.GL_FOG_START,
            float(start)
        )

        pyglet.gl.glFogf(
            pyglet.gl.GL_FOG_END,
            float(end)
        )


    @staticmethod
    def disable() -> None:
        pyglet.gl.glDisable(GL_FOG)

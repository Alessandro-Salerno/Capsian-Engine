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


import pyglet
from Capsian.video.sky_color      import SkyColorClass
from Capsian.video.scene          import Scene, Scene3D, Scene2D, OverlayScene, PlaceholderScene
from Capsian.video.camera         import PerspectiveCamera, OrthographicCamera, Camera
from Capsian.components.component import Component


CPSN_DEFAULT_DELTA_TIME   = 1/120
CPSN_DEFAULT_TEXTURE_MODE = [pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST]
CPSN_SMART_TEXTURE        = True
CPSN_NORMAL_TEXTURE       = False
CPSN_AUTO_SIZE            = None
CPSN_STANDARD_SCENE       = Scene
CPSN_3D_SCENE             = Scene3D
CPSN_GUI_SCENE            = Scene2D
CPSN_HUD_SCENE            = OverlayScene
CPSN_USELESS_SCENE        = PlaceholderScene
CPSN_AMBIENT_LIGHT        = pyglet.gl.GL_AMBIENT
CPSN_DIFFUSE_LIGHT        = pyglet.gl.GL_DIFFUSE
CPSN_SPECULAR_LIGHT       = pyglet.gl.GL_SPECULAR
CPSN_LIGHTING             = "if mode == 'enable':\n\tglEnable(GL_LIGHTING)\n\tself.lighting = True\nelse:\n\tglDisable(GL_LIGHTING)\n\tself.lighting = False"
CPSN_DEFAULT_FOG_COLOR    = [0.5, 0.69, 1.0, 1]
CPSN_DEFAULT_CLEAR_COLOR  = [0.5, 0.65, 1.0, 1.0]
CPSN_STANDARD_CAMERA      = Camera
CPSN_PERSPECTIVE_CAMERA   = PerspectiveCamera
CPSN_ORTHOGRAPHIC_CAMERA  = OrthographicCamera
CPSN_COMPONENT            = Component
CPSN_DEFAULT_FOG_START    = 40
CPSN_DEFAULT_FOG_END      = 50
CPSN_FLOAT_COLOR          = "glf"
CPSN_BYTE_COLOR           = "rgb"


class Direction:
    UP                    = "up"
    DOWN                  = "down"
    FOWARDS               = "forwards"
    BACKWARDS             = "backwards"
    LEFT                  = "left"
    RIGHT                 = "right"

    class Vector:
        UP                = [ 0.0,  0.1,  0.0 ]
        DOWN              = [ 0.0, -0.1,  0.0 ]
        LEFT              = [ 0.1,  0.0,  0.0 ]
        RIGHT             = [-0.1,  0.0,  0.0 ]
        FORWANRDS         = [ 0.0,  0.0,  0.1 ]
        BACKWARDS         = [ 0.0,  0.0, -0.1 ]


class MouseButton:
    LEFT                  = 1 << 0
    MIDDLE                = 1 << 1
    RIGHT                 = 1 << 2


lights                    = [
    pyglet.gl.GL_LIGHT0,
    pyglet.gl.GL_LIGHT1,
    pyglet.gl.GL_LIGHT2,
    pyglet.gl.GL_LIGHT3,
    pyglet.gl.GL_LIGHT4,
    pyglet.gl.GL_LIGHT5,
    pyglet.gl.GL_LIGHT6,
    pyglet.gl.GL_LIGHT7,
]

SkyColor = SkyColorClass()

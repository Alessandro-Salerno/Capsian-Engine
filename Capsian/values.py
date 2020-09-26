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
# Copyright 2019 - 2020 Alessandro Salerno (Tzyvoski)
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


from   locals                 import OpenGL
import Capsian.video.graphics as     __graphics__


CPSN_DEFAULT_DELTA_TIME   = 1/120
CPSN_WINDOW3D_GUI_MODE    = "gui"
CPSN_WINDOW3D_GAME_MODE   = "game"
CPSN_WINDOW2D_GUI_MODE    = "gui2D"
CPSN_WINDOW2D_GAME_MODE   = "game2D"
CPSN_DEFAULT_TEXTURE_MODE = [OpenGL.GL_TEXTURE_MIN_FILTER, OpenGL.GL_TEXTURE_MAG_FILTER, OpenGL.GL_NEAREST]
CPSN_SMART_TEXTURE        = True
CPSN_NORMAL_TEXTURE       = False
CPSN_AUTO_SIZE            = [None, None]
CPSN_3D_SCENE             = "game_batch"
CPSN_GUI_SCENE            = "gui_batch"
CPSN_AMBIENT_LIGHT        = OpenGL.GL_AMBIENT
CPSN_LIGHTING             = "if mode == 'enable':\n\tglEnable(GL_LIGHTING)\n\tself.lighting = True\nelse:\n\tglDisable(GL_LIGHTING)\n\tself.lighting = False"
CPSN_TRANSPARENCY         = "if mode == 'enable':\n\tglEnable(GL_BLEND)\n\tglBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)\nelse:\n\tglDisable(GL_BLEND)"
CPSN_ENHANCED_PERSPECTIVE = "if mode == 'enable':\n\tglHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)\nelse:\n\tglHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_DONT_CARE)"
CPSN_FOG                  = "if mode == 'enable':\n\tglEnable(GL_FOG)\n\tglFogfv(GL_FOG_COLOR, (GLfloat * 4)(self.fog_color[0], self.fog_color[1], self.fog_color[2], self.fog_color[3]))\n\tglHint(GL_FOG_HINT, GL_DONT_CARE)\n\tglFogi(GL_FOG_MODE, GL_LINEAR)\n\tglFogf(GL_FOG_START, self.render_distance - 10)\n\tglFogf(GL_FOG_END, self.render_distance)\n\t\nelse:\n\tglDisable(GL_FOG)"
CPSN_NICE_FOG             = "if mode == 'enable':\n\tglEnable(GL_FOG)\n\tglFogfv(GL_FOG_COLOR, (GLfloat * 4)(self.fog_color[0], self.fog_color[1], self.fog_color[2], self.fog_color[3]))\n\tglHint(GL_FOG_HINT, GL_NICEST)\n\tglFogf(GL_FOG_MODE, GL_LINEAR)\n\tglFogf(GL_FOG_START, self.render_distance - 10)\n\tglFogf(GL_FOG_END, self.render_distance)\n\t\nelse:\n\tglDisable(GL_FOG)"
CPSN_HUD_SCENE            = "hud_batch"
CPSN_DEFAULT_FOG_COLOR    = [0.5, 0.69, 1.0, 1]
CPSN_DEFAULT_CLEAR_COLOR  = [0.5, 0.65, 1.0, 1.0]
CPSN_STATIC_HUD           = "if mode == 'enable':\n\tself.render_static_hud = True\nelse:\n\tself.render_static_hud = False"
CPSN_DYNAMIC_HUD          = "if mode == 'enable':\n\tself.render_dynamic_hud = True\nelse:\n\tself.render_dynamic_hud = False"
CPSN_VERBOSE_MODE         = "for line in lines:\n\tprint(translate.build(line, mode='dont_compile'), end='')\n\ttime.sleep(0.03)"
CPSN_NORMAL_MODE          = ""


lights = [
    OpenGL.GL_LIGHT0,
    OpenGL.GL_LIGHT1,
    OpenGL.GL_LIGHT2,
    OpenGL.GL_LIGHT3,
    OpenGL.GL_LIGHT4,
    OpenGL.GL_LIGHT5,
    OpenGL.GL_LIGHT6,
    OpenGL.GL_LIGHT7
]

SkyColor = __graphics__.SkyColorClass()
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
# KeyFire Engine
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


from locals import *


class StaticLabel2D(Framework.text.Label):
    def __init__(self, font, font_size, pos, size, text, scene, color, *args, **kwargs):
        """
        Creates a text field in a 2D scene

        :param font: The font of the text
        :param font_size: The size of the font
        :param pos: The position in 2D space (Array, [x, y])
        :param size: The size (Array, [length, height]) - Set it to KFE_AUTO_SIZE for auto-size support
        :param text: The text of the label (String)
        :param scene: The Scene in which the label should be rendered (Scene())
        :param color: THe color of the text (Array, [R, G, B, A])
        """

        if scene.mode == KFE_GUI_SCENE:
            super().__init__(text=text, font_name=font, font_size=font_size, bold=False, italic=False, x=pos[0],
                             y=pos[1], width=size[0], height=size[1], batch=scene.batch, color=color, *args, **kwargs)

            graphics.stack.append(self)
        else:
            Log.critical(f"Invalid scene type {scene.mode} for Static GUI Label. This object can only be used in a GUI scene (KFE_GUI_SCENE)")


class StaticLabel3D(Framework.text.Label):
    def __init__(self, font, font_size, pos, size, text, scene, color, *args, **kwargs):
        """
        Creates a text field in a 3D scene (The text is rendered in 2D)

        :param font: The font of the text
        :param font_size: The size of the font
        :param pos: The position in 2D space (Array, [x, y])
        :param size: The size (Array, [length, height]) - Set it to KFE_AUTO_SIZE for auto-size support
        :param text: The text of the label (String)
        :param scene: The Scene in which the label should be rendered (Scene())
        :param color: THe color of the text (Array, [R, G, B, A])
        """

        if scene.mode == KFE_HUD_SCENE:
            super().__init__(text=text, font_name=font, font_size=font_size, bold=False, italic=False, x=pos[0],
                             y=pos[1], width=size[0], height=size[1], batch=scene.batch, color=color, *args, **kwargs)

            graphics.stack.append(self)
        else:
            Log.critical(f"Invalid scene type {scene.mode} for Static HUD Label. This object can only be used in a GUI scene (KFE_HUD_SCENE)")


class DynamicLabel3D(Framework.text.Label):
    """
    A dynamic label object is much more flexible than a normal one, but it comes with a performance cost

    """

    def __init__(self, font, font_size, pos, size, text, color, *args, **kwargs):
        """
        Creates a text field in a 3D scene (The text is rendered in 2D)

        :param font: The font of the text
        :param font_size: The size of the font
        :param pos: The position in 2D space (Array, [x, y])
        :param size: The size (Array, [length, height]) - Set it to KFE_AUTO_SIZE for auto-size support
        :param text: The text of the label (String)
        :param color: THe color of the text (Array, [R, G, B, A])
        """

        self.text_pointer = text

        super().__init__(text=str(text), font_name=str(font), font_size=float(font_size),
                         color=color, x=pos[0], y=pos[1], width=size[0], height=size[1], *args, **kwargs)

        graphics.dynamic_hud.append(self)
        graphics.hud_stack.__setitem__(self, self)
        graphics.stack.append(self)

        Framework.clock.schedule_interval(self.update_text, 1/5)


    def update_text(self, delta_time):
        """
        Updates the label's text. This is used for multiple reasons:
        1. Setting the text when the label is created
        2. Updating the text if a pointer (Such as Framework.clock.get_fps) is specified in the text propriety

        :param delta_time:
        :return: Nothing
        """

        try:
            self.text = str(self.text_pointer())
        except:
            try:
                self.text = str(self.text_pointer)
            except:
                self.text = "DynamicLabel3D"


    def move_to(self, x, y):
        """
        Moves the label to the given coordinates.

        :param x: The new x position
        :param y: The new y position
        :return: Nothing
        """

        self.x = int(x)
        self.y = int(y)

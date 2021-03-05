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


from   Capsian.log                  import Log
from   Capsian.values               import CPSN_HUD_SCENE
from   Capsian.components.transform import Transform
from   Capsian.video.scene          import PlaceholderScene
import Capsian.engine               as     engine
import pyglet


class Label(pyglet.text.Label):
    """
    Fields
    ------
        scene | A Capsian Scene Object | Scene2D/OverlayScene

    Methods
    -------
        move_to | Moves the label to the specified position
    """

    def __init__(self, font: str, font_size: float, text: str, color, transform=Transform(), scene=PlaceholderScene(), *args, **kwargs):
        """
        Parameters
        ----------
            font      | The font you want to use for the label          | str
            font-size | The font size you want to use                   | float
            text      | The text of the label                           | str
            color     | The color of the label                          | list [R, G, B, A]
            scene     | The Capsian Scene of which the label is part of | Scene2D
        """

        if not isinstance(scene, CPSN_HUD_SCENE):
            Log.critical(f"Invalid scene type for Static HUD Label. This object can only be used in a GUI scene (CPSN_HUD_SCENE)")
            return

        self.scene = scene

        super().__init__(
            text=text,
            font_name=font,
            font_size=font_size,
            bold=False,
            italic=False,
            x=transform.x,
            y=transform.y,
            width=transform.width,
            height=transform.height,
            color=color,
            *args, **kwargs
        )


    def move_to(self, x: int, y: int) -> None:
        """
        Parameters
        ----------
            x | The new X position | int
            y | The new Y position | int
        """

        self.x = int(x)
        self.y = int(y)


####################################################################


class Label2D(Label):
    """
    Fields
    ------
        scene | A Capsian Scene Object | Scene2D/OverlayScene

    Methods
    -------
        move_to | Moves the label to the specified position
    """
    
    def __init__(self, font: str, font_size: float, text: str, color, transform=Transform(), scene=PlaceholderScene, *args, **kwargs):
        """
        Parameters
        ----------
            font      | The font you want to use for the label          | str
            font-size | The font size you want to use                   | float
            text      | The text of the label                           | str
            color     | The color of the label                          | list [R, G, B, A]
            scene     | The Capsian Scene of which the label is part of | Scene2D
        """

        super().__init__(
            font=font,
            font_size=font_size,
            transform=transform,
            text=text,
            scene=scene,
            color=color,
            *args, **kwargs
        )

        self.scene.dynamic_gui.append(self)


class Label3D(Label):
    """
    Fields
    ------
        scene | A Capsian Scene Object | Scene2D/OverlayScene

    Methods
    -------
        move_to | Moves the label to the specified position
    """

    def __init__(self, font: str, font_size: float, text: str, color, transform=Transform(), scene=PlaceholderScene, *args, **kwargs):
        """
        Parameters
        ----------
            font      | The font you want to use for the label          | str
            font-size | The font size you want to use                   | float
            text      | The text of the label                           | str
            color     | The color of the label                          | list [R, G, B, A]
            scene     | The Capsian Scene of which the label is part of | Scene2D
        """

        super().__init__(
            font=font,
            font_size=font_size,
            transform=transform,
            text="",
            scene=scene,
            color=color,
            *args, **kwargs
        )

        self.text_pointer = text
        scene.dynamic_hud.append(self)
        engine.default_clock.Schedule.call_with_interval(self.update_text, 1/10)


    def update_text(self, dt: float) -> None:
        """
        Updates the label's text. This is used for multiple reasons:
        1. Setting the text when the label is created
        2. Updating the text if a pointer (Such as pyglet.clock.get_fps) is specified in the text propriety

        :param delta_time:
        :return: None
        """

        try:
            self.text     = str(self.text_pointer())
        except TypeError:
            self.text = str(self.text_pointer)
        except:
            self.text = "Invalid Pointer!"

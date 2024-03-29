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


from   Capsian.components.component import Component
import Capsian.engine             as engine


class MouseInputHandler(Component):
    """
    Fields
    ------
        pressed_button      | The currently pressed button (button held) | Pyglet Mouse State Handler
        mouse_state_handler | The Mouse State Handler for the object     | CapsianMouseStateHandlerObject

    Methods
    -------
        on_button_pressed  | What happens when a button is pressed
        on_button_released | What happens when a button is released
        on_button_held     | What happens when a button is held down
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self):
        from pyglet.window.mouse import MouseStateHandler

        class CapsianMouseStateHandlerObject(MouseStateHandler):
            def __init__(self, parent):
                self.parent = parent
                super().__init__()

            def on_mouse_press(self, x, y, button, modifiers):
                self.parent.on_button_pressed(x, y, button, modifiers)

            def on_mouse_release(self, x, y, button, modifiers):
                self.parent.on_button_released(x, y, button, modifiers)

            def __eq__(self, value):
                return self[value]

        
        self.pressed_button      = MouseStateHandler()
        self.mouse_state_handler = CapsianMouseStateHandlerObject(self)

        engine.main_window.push_handlers(self.pressed_button)
        engine.main_window.push_handlers(self.mouse_state_handler)

        super().__init__()


    def __repr__(self):
        return "mouse_listener"


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def on_button_pressed(self, x: int, y: int, button, modifiers):
        """
        Parameters
        ----------
            x         | The cursor's X position          | int
            y         | The cursor's Y position          | int
            button    | The button that is being pressed
            modifiers | The modifiers applied to the stroke
        """

        pass


    def on_button_released(self, x: int, y: int, button, modifiers):
        """
        Parameters
        ----------
            x         | The cursor's X position          | int
            y         | The cursor's Y position          | int
            button    | The button that is being pressed
            modifiers | The modifiers applied to the stroke
        """

        pass


    def on_button_held(self, buttons):
        """
        Parameters
        ----------
            buttons | All the buttons | dict
        """

        pass


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_update(self, dt: float, time):
        self.on_button_held(self.pressed_button)

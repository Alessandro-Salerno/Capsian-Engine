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
from pyglet.window import key


class KeyboardInputHandler(Component):
    """
    A Keyboard Input Handler is an abstract object that does not have a position in the world.
    Instead, it's a series of functions that allow you to register nd check keystrokes.
    It can be used for loads of things, but it's not the only option available in Capsian
    """

    def __init__(self):

        class CapsianKeyStateHandlerObject(Key.KeyStateHandler):
            def __init__(self, parent):
                self.parent = parent
                super().__init__()

            def on_key_press(self, symbol, modifiers):
                self.parent.on_key_pressed(symbol, modifiers)

            def on_key_release(self, symbol, modifiers):
                self.parent.on_key_released(symbol, modifiers)

            def __eq__(self, value):
                return self.get(value)


        self.pressed_key       = Key.KeyStateHandler()
        self.key_state_handler = CapsianKeyStateHandlerObject(self)

        engine.main_window.push_handlers(self.pressed_key)
        engine.main_window.push_handlers(self.key_state_handler)

        super().__init__()
        self.enable()
    

    def on_key_pressed(self, symbol, modifiers):
        """
        What happens when a single key is pressed
        This method is called by a sub-class of KeyboardInputHandler() that acts as a pyglet KeyStateHandler()

        :return: None
        """

        pass


    def on_key_released(self, symbol, modifiers):
        """
        What happens when a single key is released
        This method is called by a sub-class of KeyboardInputHandler() that acts as a pyglet KeyStateHandler()

        :return: None
        """

        pass


    def on_key_held(self, keys):
        """
        What happens when a key is held down.
        This method is called by the KeyboardInputHandler Component's parent class trhough the component's on_update mathod

        :return: None
        """

        pass


    def on_update(self, dt, time):
        self.on_key_held(self.pressed_key)


    def __repr__(self):
        return "key_listener"

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
#  * Redistributioans of source code must retain the above copyright
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


import math
import Capsian.maths.math         as kmath
from Capsian.components.component import Component
from Capsian.log                  import Log
from Capsian.values               import CPSN_PERSPECTIVE_CAMERA
import Capsian.engine             as engine


class CharacterController(Component):
    """
    A Character Controller surves a very important function: moving and rotating the camera.
    It does so via commands sent by your code nad by the engine itself.

    It's a component, as such it must be added to a Camera entity in order to function.
    IN the future, you'll be able to add a Character Controller to any entity but for now compatibility is scarse... 
    """

    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self):
        self.multiplier = 50.00
        self.dividend   = 10.00
        self.sens       = 1.000
        self.speed      = 0.100
        self.s          = 0.000

        super().__init__()


    def __repr__(self):
        return "character_controller"


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_ready(self, time):
        if not isinstance(self.parent, CPSN_PERSPECTIVE_CAMERA):
            Log.critical("You are trying to add a CharacterController Component to an object that is not CPSN_PERSPECTIVE_CAMERA compatible")
            return
        
        super().on_ready(time)


    def on_update(self, dt, time):
        self.s              = dt     * self.multiplier * engine.main_window.alive

        self.parent.rotY    = -self.parent.components.transform.rotY / 180 * math.pi

        self.parent.dx      = self.s * math.sin(self.parent.rotY)
        self.parent.dz      = self.s * math.cos(self.parent.rotY)


    def rotate(self):
        self.parent.components.transform.rotX  += self.parent.mouse_dy * self.sens
        self.parent.components.transform.rotY  -= self.parent.mouse_dx * self.sens

        self.parent.components.transform.rotX   = kmath.clamp(90, -90, self.parent.components.transform.rotX)


    def move(self, direction):
        """
        This method actually moves the camera, it's called by your input handler

        :param direction: The direction in which the camera should move (String)
        :return: None
        """

        if direction    == "forwards":
            self.parent.components.transform.x += self.parent.dx * self.speed * engine.main_window.alive
            self.parent.components.transform.z -= self.parent.dz * self.speed * engine.main_window.alive

        if direction    == "backwards":
            self.parent.components.transform.x -= self.parent.dx * self.speed * engine.main_window.alive
            self.parent.components.transform.z += self.parent.dz * self.speed * engine.main_window.alive

        if direction    == "right":
            self.parent.components.transform.x += self.parent.dz * self.speed * engine.main_window.alive
            self.parent.components.transform.z += self.parent.dx * self.speed * engine.main_window.alive

        if direction    == "left":
            self.parent.components.transform.x -= self.parent.dz * self.speed * engine.main_window.alive
            self.parent.components.transform.z -= self.parent.dx * self.speed * engine.main_window.alive

        if direction    == "down":
            self.parent.components.transform.y -= self.s / self.dividend * engine.main_window.alive

        if direction    == "up":
            self.parent.components.transform.y += self.s / self.dividend * engine.main_window.alive

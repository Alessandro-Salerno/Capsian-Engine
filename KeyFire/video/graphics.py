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


from locals import Log

####################################################################################################################################################################################################################################################################################
#
#       UNIVERSAL UTILITIES
#
####################################################################################################################################################################################################################################################################################

view = {
    "Camera": 0,
    "Window": 0
}

scenes = []
gui_scenes = []
hud_scenes = []
dynamic_hud = []
hud_stack = {}
objects2D = []
gui_pos = {}
lights = []
stack = []


####################################################################################################################################################################################################################################################################################
#
#       RENDERING
#
###################################################################################################################################################################################################################################################################################


def draw():
    """
    This function calls all draw methods (For objects, particles, lights ecc)

    :return:
    """

    for scene in scenes:
        scene.batch.draw()

    for object2D in objects2D:
        if object2D.is_visible():
            object2D.quad()

    for light in lights:
        light.draw()


def draw_gui():
    """
    Calls all GUI draw methods (label ecc)

    :return:
    """

    for gui_scene in gui_scenes:
        gui_scene.batch.draw()


def draw_hud():
    """
    Draws all the static HUD in the scene

    :return: Nothing
    """

    for hud_scene in hud_scenes:
        hud_scene.batch.draw()


def draw_dynamic_hud():
    """
    Draws the dynamic HUD in a scene

    :return: Nothing
    """

    for hud in dynamic_hud:
        hud.draw()

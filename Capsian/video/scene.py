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


from locals import*


class Scene:
    def __init__(self, camera, mode=CPSN_3D_SCENE):
        """
        Creates a Capsian scene object.
        It uses pyglet.graphics.Batch()

        :param mode: The Scene mode (CPSN_3D_SCENE or CPSN_GUI_SCENE)
        """
        
        # Set mode
        self.mode        = mode
        self.camera      = camera

        # Check mode
        if mode     == CPSN_3D_SCENE:
            if repr(camera) == CPSN_PERSPECTIVE_CAMERA:
                camera.scenes.append(self)
            else:
                Log.critical("Cannot add 3D scene to non-perspective camera. Please pass a perspective camera, not a generic or orthographic one")
        else:
            if mode == CPSN_GUI_SCENE:
                if repr(camera) == CPSN_ORTHOGRAPHIC_CAMERA:
                    camera.scenes.append(self)
                else:
                    Log.critical("Cannot add GUI scene to non-orthographic camera. Please pass an orthographic camera, not a generic or perspective one")
            else:
                if repr(camera) == CPSN_PERSPECTIVE_CAMERA:
                    camera.hud_scenes.append(self)

        # Defines lists of objects
        self.batch       = Framework.graphics.Batch()
        self.hud_batch   = Framework.graphics.Batch()
        self.objects2D   = types.LimitedLenghtObjectArray(750.000, True)
        self.dynamic_gui = types.LimitedLenghtObjectArray(200.000, True)
        self.dynamic_hud = types.LimitedLenghtObjectArray(30.0000, True)
        self.lights      = types.LimitedLenghtObjectArray(8.00000, True)
        self.stack       = types.LimitedLenghtObjectArray(1000.00, True)
        
        self.stack.append(camera)


    # Adds somethings to the batch
    def add(self, *args, **kwargs):
        self.batch.add(*args, **kwargs)


    def disable(self):
        if self.mode == CPSN_3D_SCENE or self.mode == CPSN_GUI_SCENE:
            self.camera.scenes.remove(self)
        elif self.mode == CPSN_HUD_SCENE:
            self.camera.hud_scenes.remove(self)
        
        Log.warning(f"Scene {self} removed from camera {self.camera}!")


    def enable(self):
        if self.mode == CPSN_3D_SCENE or self.mode == CPSN_GUI_SCENE:
            self.camera.scenes.append(self)
        elif self.mode == CPSN_HUD_SCENE:
            self.camera.hud_scenes.append(self)

        Log.warning(f"Scene {self} added to camera {self.camera}!")


    def __repr__(self):
        return "Capsian Standard Scene"

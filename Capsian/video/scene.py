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


from   Capsian.log     import Log
import Capsian.types   as types
import pyglet


class Scene:
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, camera):
        """
        Parameters
        ----------
            camera | A Camera Object | Camera\OrthographicCamera\PerspectiveCamera
        """
        
        self.camera      = camera
        self.enabled     = False

        # Defines lists of objects
        self.batch       = pyglet.graphics.Batch()
        self.lights      = types.LimitedLenghtObjectArray(8.00000, False)
        self.stack       = types.LimitedLenghtObjectArray(1000.00, False)
        self.objects2D   = list()
        self.drawable    = list()
        
        self.stack.append(camera)


class Scene3D(Scene):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, camera):
        from Capsian.values import CPSN_PERSPECTIVE_CAMERA

        super().__init__(camera)

        if not isinstance(camera, CPSN_PERSPECTIVE_CAMERA):
            Log.critical(f"{repr(camera)} is not a valid camera for Scene3D!")
            return
        
        if not self.enable():
            Log.error(f"Could not enable scene {self}")


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def disable(self) -> bool:
        if not self.enabled:
            Log.error(f"Scene {self} already disabled")
            return False

        self.camera.scenes.remove(self)
        return True

    
    def enable(self) -> bool:
        if self.enabled:
            Log.error(f"Scene {self} already enabled")
            return False

        self.camera.scenes.append(self)
        return True


class Scene2D(Scene):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, camera):
        from Capsian.values import CPSN_ORTHOGRAPHIC_CAMERA
        
        super().__init__(camera)

        self.dynamic_gui = types.LimitedLenghtObjectArray(200.000, False)

        if not isinstance(camera, CPSN_ORTHOGRAPHIC_CAMERA):
            Log.critical(f"{repr(camera)} is not a valid camera for Scene2D!")
            return
        
        if not self.enable():
            Log.error(f"Could not enable scene {self}")


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def disable(self) -> bool:
        if not self.enabled:
            Log.error(f"Scene {self} already disabled")
            return False

        self.camera.scenes.remove(self)
        return True

    
    def enable(self) -> bool:
        if self.enabled:
            Log.error(f"Scene {self} already enabled")
            return False

        self.camera.scenes.append(self)
        return True


class OverlayScene(Scene):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, camera):
        from Capsian.values import CPSN_HUD_SCENE, CPSN_PERSPECTIVE_CAMERA

        super().__init__(camera)

        self.hud_batch   = pyglet.graphics.Batch()
        self.dynamic_hud = types.LimitedLenghtObjectArray(30.0000, False)

        if not isinstance(camera, CPSN_PERSPECTIVE_CAMERA):
            Log.critical(f"{repr(camera)} is not a valid camera for OverlayScene!")
            return
        
        if not self.enable():
            Log.error(f"Could not enable scene {self}")


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def disable(self) -> bool:
        if not self.enabled:
            Log.error(f"Scene {self} already disabled")
            return False

        self.camera.hud_scenes.remove(self)
        return True

    
    def enable(self) -> bool:
        if self.enabled:
            Log.error(f"Scene {self} already enabled")
            return False

        self.camera.hud_scenes.append(self)
        return True


class PlaceholderScene(Scene):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self):
        from Capsian.values import CPSN_STANDARD_SCENE
        super().__init__(None)

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


from locals import *
from Capsian.components.transform import Transform


class Entity:
    """
    A Capsian Entity.
    An Entity is generally used as a parent class for entities. 
    """

    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=Transform(), scene=None, active=False):
        """
        Creates an entity in the world
        This is usually used as super/parent class for other entitys like Cubes

        :param size: The size of the entity (Array, [width, height, depth])
        :param pos: The position of the world in 3 Space (Array, [x, y, z])
        :param rot: The rotation of the entity (Array, [x, y])
        :param batch: The scene in which the entity should be rendered
        """

        from datetime import datetime

        class Components(list):
            transform            = None
            character_controller = None
            key_listener         = None
            mouse_listener       = None


            def __init__(self, spr):
                self.spr = spr


            def add(self, component):
                from datetime import datetime

                component._init(self.spr)
                self.append(component)
                self.spr.on_component_added(datetime.now())
                setattr(self, repr(component), component)
                component.on_ready(datetime.now())


        self.components = Components(self)
        self.active     = active
        self.components.add(transform)

        if not repr(scene) == CPSN_STANDARD_SCENE:
            self.scene = None
            return

        if scene == None:
            from Capsian.video.scene import PlaceholderScene
            self.scene = PlaceholderScene()
            return

        self.scene  = scene

        if active: scene.stack.append(self)
        self.on_create(datetime.now())


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_start(self, time):
        """
        What happens when the program starts
        """

        return False


    def on_update(self, dt, time):
        """
        What happens when the program updates
        """

        for component in self.components:
            component.update(dt)


    def on_fixed_update(self, dt, time):
        """
        What happens when the fixed_update function passes through this entity
        """

        return False


    def on_close(self, time):
        """
        What happens when the program closes
        """

        return False

    
    def on_create(self, time):
        """
        what happens when the entity is created
        """

        return False

    
    def on_destroy(self, time):
        """
        what happens when the entity is destroied
        """

        return False


    def on_duplicate(self, time):
        """
        What happens when the entity is duplicated.
        """

        return False


    def on_enable(self, time):
        """
        What happens when the entity is enabled
        """

        return False

    
    def on_disable(self, time):
        """
        What happens when the entity is disabled 
        """

        return False


    def on_component_added(self, time):
        """
        What happens when a component is added to this entity
        """

        return False


    # -------------------------
    #
    #       PROPERTIES
    #
    # -------------------------

    @property
    def entity_type(self):
        return repr(self)


    # -------------------------
    #
    #       OTHER METHODS
    #
    # -------------------------

    def duplicate(self):
        import copy
        from datetime import datetime

        self.on_duplicate(datetime.now())
        return copy.deepcopy(self)


    def update(self, dt):
        from datetime import datetime
        self.on_update(dt, datetime.now())

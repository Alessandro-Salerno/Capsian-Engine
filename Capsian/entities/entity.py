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


from Capsian.components.transform import Transform
from Capsian.components.component import Component


class Entity:
    """
    A Capsian Entity.
    An Entity is generally used as a parent class for entities. 

    Fields
    ------
        components | The components object that holds data about the entity's components | Components
        active     | Weather the entity is active or not                                 | bool
        scene      | The Scene of which the entity is a part of                          | Scene2D/Scene3D/OverlayScene

    Methods
    -------
        on_update          | What happens when the entity is updated by the clock
        on_fixed_update    | What happens when the entity is updated by a fixed updater
        on_create          | What happens when the entity is created
        on_destroy         | What happens when the entity is deleted
        on_duplicate       | What happens when the entity is duplicated
        on_enable          | What happens when the entity is enabled
        on_disable         | What happens when the entity is disabled
        on_component_added | What happens when a component is added to the entity
        duplicate          | Duplicates the entity
        update             | Sends an update signal to the entity
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=Transform(), scene=None, active=False):
        """
        Parameters
        ----------
            transform | A Capsian Transform Component       | Transform
            scene     | A Capsian Scene Object              | Scene2D/Scene3D/OverlayScene
            active    | Weather the entity is active or not | bool
        """

        from datetime       import datetime
        from Capsian.values import CPSN_STANDARD_SCENE

        class Components(list):
            transform            = None
            character_controller = None
            key_listener         = None
            mouse_listener       = None


            def __init__(self, spr: Entity):
                self.spr = spr


            def add(self, component: Component) -> None:
                from datetime import datetime

                component._init(self.spr)
                self.append(component)
                self.spr.on_component_added(component, datetime.now())
                setattr(self, repr(component), component)
                component.on_ready(datetime.now())

            
            def component(self, **kwargs):
                import inspect

                def inner(component):
                    if not inspect.isclass(component):
                        if not isinstance(component, Component):
                            return

                        self.add(component)
                        return

                    try:
                        self.add(component(**kwargs))
                    except TypeError:
                        self.add(component())
                    except:
                        pass

                return inner


        self.components = Components(self)
        self.active     = active
        self.components.add(transform)

        self.next_pos = [
            [transform.x + 1,  transform.y    ,  transform.z    ],
            [transform.x - 1,  transform.y    ,  transform.z    ],
            [transform.x    ,  transform.y    ,  transform.z + 1],
            [transform.x    ,  transform.y    ,  transform.z - 1],
            [transform.x    ,  transform.y + 1,  transform.z    ],
            [transform.x    ,  transform.y - 1,  transform.z    ],
        ]

        self.scene  = scene

        if not isinstance(scene, CPSN_STANDARD_SCENE):
            self.scene = None
            return

        if scene == None:
            from Capsian.video.scene import PlaceholderScene
            self.scene = PlaceholderScene()

        if active:
            scene.stack.append(self)
        
        self.on_create(datetime.now())


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_update(self, dt: float, time) -> None:
        """
        Parameters
        ----------
            dt   | The delta time sent from the clock | float
            time | The current date and time
        """

        for component in self.components:
            component.update(dt)


    def on_fixed_update(self, dt: float, time) -> bool:
        """
        Parameters
        ----------
            dt   | The delta time sent from the clock | float
            time | The current date and time
        """

        return False

    
    def on_create(self, time) -> bool:
        """
        Parameters
        ----------
            time | The current date and time
        """

        return False

    
    def on_destroy(self, time) -> bool:
        """
        Parameters
        ----------
            time | The current date and time
        """

        return False


    def on_duplicate(self, time) -> bool:
        """
        Parameters
        ----------
            time | The current date and time
        """

        return False


    def on_enable(self, time) -> bool:
        """
        Parameters
        ----------
            time | The current date and time
        """

        return False

    
    def on_disable(self, time) -> bool:
        """
        Parameters
        ----------
            time | The current date and time
        """

        return False


    def on_component_added(self, component: Component, time) -> bool:
        """
        Parameters
        ----------
            component | A pointer to the component that has been added | Component
            time      | The current date and time
        """

        return False


    # -------------------------
    #
    #       OTHER METHODS
    #
    # -------------------------

    def duplicate(self) -> None:
        import copy
        from datetime import datetime

        self.on_duplicate(datetime.now())
        return copy.deepcopy(self)


    def update(self, dt: float) -> None:
        from datetime import datetime
        self.on_update(dt, datetime.now())

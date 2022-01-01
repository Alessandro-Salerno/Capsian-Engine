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


from Capsian.log             import Log
import Capsian.engine        as     engine


class Component:
    """
    A Capsian Entity Component is an object (In OOP sense) that can be added to an Entity (An in-game Object)
    to extend the features of the Entity. 

    Properties
    ----------
        enable | Weather the component is enabled or not | bool
        parent | The compnent's parent object            | Entity

    Methods
    -------
        on_start        | What happens the program start
        on_update       | What happens when the component recieves an update from an Entity
        on_fixed_update | What happens when the recieves a fixed update from the clock
        on_close        | What happens the progam ends
        on_create       | What happens when the component is initiated
        on_destroy      | What happens when the component is deleted
        on_ready        | What happens when the component is added to an entity
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self):
        from datetime import datetime

        self.on_create(datetime.now())

        engine.default_clock.entry_points.add(self.on_start)
        engine.default_clock.exit_points.add(self.on_close)

        self._parent  = None


    def __repr__(self):
        return "Capsian EntityComponent"


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_start(self, time) -> bool:
        """
        This method is called when the game starts.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            time | The current date and time
        """

        return False


    def on_update(self, dt: float, time) -> bool:
        """
        This method is called every time the parent object's update mathod is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            dt   | The deltatime passed by the engine | float < 1.0
            time | The current date and time
        """

        return False


    def on_fixed_update(self, dt: float, time):
        """
        This method is called every time the parent object's fixed update mathod is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            dt   | The deltatime passed by the engine | float < 1.0
            time | The current date and time
        """

        return False


    def on_close(self, time) -> bool:
        """
        This method is called when the parent object's on close mathod is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            time | The current date and time
        """

        return False

    
    def on_create(self, time) -> bool:
        """
        This method is called when the component's _init__ method is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            time | The current date and time
        """

        return False

    
    def on_destroy(self, time) -> bool:
        """
        This method is called when the component's __del__ method is. 
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            time | The current date and time
        """

        return False


    def on_ready(self, time) -> bool:
        """
        This method is called when the component is added to an entity.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        Parameters
        ----------
            time | The current date and time
        """

        return False


    # -------------------------
    #
    #       PROPERTIES
    #
    # -------------------------
    
    @property
    def parent(self):
        return self._parent


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def update(self, dt: float) -> None:
        from datetime import datetime
        self.on_update(dt, datetime.now())


    # -------------------------
    #
    #       PRIVATE METHODS
    #
    # -------------------------

    def _init(self, parent) -> None:
        self._parent = parent

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


class Component:
    """
    A Capsian Entity Component is an object (In OOP sense) that can be added to an Entity (An in-game Object)
    to extend the features of the Entity. 
    """

    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self):
        from datetime import datetime

        self.on_create(datetime.now())
        engine.entries + self.on_start
        engine.exits + self.on_close

        self._enabled = False
        self._parent  = None


    def __repr__(self):
        return "Capsian EntityComponent"


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_start(self, time):
        """
        This method is called when the game starts.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False


    def on_update(self, dt, time):
        """
        This method is called every time the parent object's update mathod is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param dt: The deltatime provided by the pyglet clock
        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False


    def on_fixed_update(self, dt, time):
        """
        This method is called every time the parent object's fixed update mathod is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param dt: The deltatime provided by the pyglet clock
        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False


    def on_close(self, time):
        """
        This method is called when the parent object's on close mathod is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False

    
    def on_create(self, time):
        """
        This method is called when the component's _init__ method is.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False

    
    def on_destroy(self, time):
        """
        This method is called when the component's __del__ method is. 
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False


    def on_ready(self, time):
        """
        This method is called when the component is added to an entity.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        if self.on_update(0, 0) is not False:
            self.enable()


    def on_enable(self, time):
        """
        This method is called when the component is enabled.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """
        return False

    
    def on_disable(self, time):
        """
        This method is called when the component is disabled.
        By default it only returns False, but it can (And should) be overriden to do something.
        You can also just remove it from your component as it will still be present in the base class which means you're not gonna have any issues. 

        :param time: The exact date and time of when the method was called
        :return: False (By Default)
        """

        return False


    # -------------------------
    #
    #       PROPERTIES
    #
    # -------------------------
    
    @property
    def enabled(self):
        return self._enabled


    @property
    def parent(self):
        return self._parent


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def enable(self):
        from datetime import datetime

        if not self._enabled:
            self._enabled = True
            Framework.clock.schedule(self.update)
            self.on_enable(datetime.now())
        else:
            Log.error("Component already enabled!")


    def disable(self):
        from datetime import datetime

        if self._enabled:
            self._enabled = False
            Framework.clock.unschedule(self.on_update)
            self.on_disable(datetime.now())
        else:
            Log.error("Component already disabled!")


    def update(self, dt):
        from datetime import datetime
        self.on_update(dt, datetime.now())


    # -------------------------
    #
    #       PRIVATE METHODS
    #
    # -------------------------

    def _init(self, parent):
        self._parent = parent
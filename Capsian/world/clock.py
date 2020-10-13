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


class Clock:
    """
    A Capsian Clock isn implementation of pyglet.clock.Clock (Framework.clock.Clock)
    """


    def __init__(self):
        self.Schedule.call_every_tick(self.tick)


    class _EntryPoints:
        """
        A class that holds data about all entry points
        """


        def __init__(self, objs):
            self.objs = []

            for obj in list(objs):
                try:
                    if self.validate(obj):
                        self.objs.append(obj)
                except:
                    continue


        def __add__(self, obj):
            self.add(obj)


        def add(self, obj):
            if self.validate(obj):
                self.objs.append(obj)


        def validate(self, obj):
            return repr(obj) == "EntryPoint Object"


        def call(self):
            for obj in self.objs:
                obj.func()



    class EntryPoint:
        """
        A class that holds data about one entry point
        """


        def __init__(self, clock, func):
                self.clock = clock
                self.func  = func


        def __repr__(self):
                return "EntryPoint Object"


    

    class _ExitPoints:
        """
        A class that holds data about all exit points
        """


        def __init__(self, objs):
            self.objs = []

            for obj in list(objs):
                try:
                    if self.validate(obj):
                        self.objs.append(obj)
                except:
                    continue


        def __add__(self, obj):
            self.add(obj)


        def add(self, obj):
            if self.validate(obj):
                self.objs.append(obj)


        def validate(self, obj):
            return repr(obj) == "ExitPoint Object"


        def call(self):
            for obj in self.objs:
                obj.func()



    class ExitPoint:
        """
        A class that holds data about an exit point
        """


        def __init__(self, clock, func):
                self.clock = clock
                self.func  = func


        def __repr__(self):
                return "EntryPoint Object"




    class Schedule:
        """
        A class that takes care of scheduling using the implementation of a pyglet clock
        """


        @staticmethod
        def call_every_tick(func, *args, **kwargs):
            Framework.clock.schedule(func, *args, **kwargs)


        @staticmethod
        def call_with_interval(func, interval, *args, **kwargs):
            Framework.clock.schedule_interval(func, interval, *args, **kwargs)


        @staticmethod
        def wait(milliseconds):
            Framework.clock.Clock.sleep(milliseconds * 1000)




    entry_points = _EntryPoints([])
    exit_points  = _ExitPoints([])


    def tick(self, dt):
        from locals import engine

        for scene in engine.main_camera.scenes:
            for obj in scene.stack:
                obj.update(dt)

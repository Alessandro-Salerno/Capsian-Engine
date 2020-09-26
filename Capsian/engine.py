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


from locals                   import *
import Capsian.video.graphics as graphics

# Declare vars
main_window       = None
main_camera       = None
main_key_listener = None
scheduled         = []
entry_points      = []
exit_points       = []


def update(dt):
    """
    This function runs in the background ever 120th of a second.
    It's used to update the pyglet clock and call all the looping functions in the stack

    :return: None
    """

    Framework.clock.tick()

    for func in scheduled:
        func(dt)


# Prepares the application
def run():
    """
    Starts the engine and (Ironically) also stops it

    :return: None
    """

    from datetime import datetime

    for fn in entry_points:
        try:
            fn(datetime.now())
        except:
            try:
                fn()
            except:
                Log.critical(f"Unable to call {fn} as entry point")
    
    Framework.app.run()
    
    for fn in exit_points:
        try:
            fn(datetime.now())
        except:
            try:
                fn()
            except:
                Log.critical(f"There is something wrong with {fn}")

    Framework.app.exit()


class Scheduled:
    """
    This is a lower level class not directly exposed to the scripting library.
    It's used to add and remove looping functions from a stack.
    'engine.loops' is an instance of this class
    """


    def __add__(self, func=(None, 1/120)):
        self.add(func[0], func[1])

    def __sub__(self, func):
        self.remove(func)


    def add(self, func, dt=1/120):
        if dt == 1/120:
            scheduled.append(func)
        else:
            Framework.clock.schedule_interval(func, dt)


    def remove(self, func):
        if func in scheduled:
            scheduled.remove(func)
        else:
            try:
                Framework.clock.unschedule(func)
            except:
                Log.critical(f"{func} is not scheduled, thus it can not be unscheduled")


class EntryPoints:
    """
    This class is used to add entry points
    EPs are functions called when the program starts, in this case, they're user defined.
    These functions run when engine.run() i s called in main.py
    """


    def __add__(self, other):
        self.add(other)


    def add(self, other):
        entry_points.append(other)


class ExitPoints:
    """
    This class is used to add exit points.
    Exit points are functions called when the program ends, in this case they're user defined.
    They are called before Framework.app.exit() in engine.run()(Here in engine.py)
    """


    def __add__(self, other):
        self.add(other)

    def add(self, other):
        exit_points.append(other)


loops   = Scheduled()
entries = EntryPoints()
exits   = ExitPoints()
Framework.clock.schedule_interval(update, 1 / 120)

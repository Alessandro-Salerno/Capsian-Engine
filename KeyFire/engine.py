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


from locals import *
import KeyFire.video.graphics as graphics

frames = []
functions = {
    "run": False,
    "update_function": None,
    "end_function": None
}


# Calls s the main function in the script
def start(main_function, update_function, end_function):
    main_function()

    functions.__setitem__("update_function", update_function)
    functions.__setitem__("end_function", end_function)
    functions.__setitem__("run", True)


# Get frame-rate
def frame_rate(delta_time):
    if get_main_window().alive > 0:
        fps = Framework.clock.get_fps()
        frames.append(fps)
        Log.info(f"{round(fps)} FPS")


# Ticks
def update(delta_time):
    Framework.clock.tick()

    if functions.get("run"):
        get_update_function()()


# Returns the main camera used in the application
def get_main_camera():
    return graphics.view.get("Camera")


# Returns the main window of the applicatin
def get_main_window():
    return graphics.view.get("Window")


# Returns the update function
def get_update_function():
    return functions.get("update_function")


# Returns the end function of the program
def get_end_function():
    return functions.get("end_function")


# Set switch main camera
def set_main_camera(new_camera):
    graphics.view.__setitem__("Camera", new_camera)
    get_main_window().view_port = new_camera


# Prepares the application
def run():
    Framework.app.run()

    try:
        print("Highest frame-rate: ", max(frames))
        total = sum(frames)
        avg = total / len(frames)
        print("Avg frame-rate: ", avg)
        frames.sort()
        print("Lowest frame-rate: ", *frames[:1])
        print("Running pyglet version: ", Framework.version)
    except:
        Log.error("Unable to determine frame-rates")

    for obj in graphics.stack:
        obj

    graphics.stack.clear()
    Log.warning("Deleted all objects from the KeyFire Stack")

    get_end_function()()

    Framework.app.exit()


Framework.clock.schedule_interval(update, 1 / 120)
Framework.clock.schedule_interval(frame_rate, 1)

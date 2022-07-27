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


from turtle import width
from   capsian  import *
from   os      import system
import os
import sys
import json


class Capsianline:
    @staticmethod
    def capsianline():
        return 0


# Main function
def main(argv: list) -> int:
    # Simple command
    if len(argv) >= 2 and hasattr(Capsianline, str(argv[1]).replace("--", "")):
        getattr(Capsianline, str(argv[1]).replace("--", ""))(*argv[2:])
        return 0

    # Eval the contens of the options file
    with open("capsian.json", "r") as preferences:
        global options
        _options = preferences.read()
        options  = json.loads(_options)

    # Import the Capsian Project
    __import__(options["project"]["package"])

    try:
        # Camera setup
        cmtype = options["camera"]["type"]
        camera = PerspectiveCamera() if cmtype == "perspective" else OrthographicCamera()
    
        camera.components.transform.x = options["camera"]["position"]["x"]
        camera.components.transform.y = options["camera"]["position"]["y"]
        camera.components.transform.z = options["camera"]["position"]["z"]

        camera.components.transform.rotX = options["camera"]["rotation"]["x"]
        camera.components.transform.rotY = options["camera"]["rotation"]["y"]
        camera.components.transform.rotZ = options["camera"]["rotation"]["z"]

        camera.fov  = options["camera"]["fov"]
        camera.far  = options["camera"]["far"]
        camera.near = options["camera"]["near"]

        # Window setup
        window = Window3D(
            camera=camera,
            width=options["window"]["width"] if options["window"]["width"] != 0 else None,
            height=options["window"]["height"] if options["window"]["height"] != 0 else None,
            fullscreen=options["window"]["fullscreen"],
            vsync=options["window"]["vsync"]
        )

        # Enable Capsian Basic Lighting if required
        if options["lighting"]["enabled"]:
            engine.main_window.enable(CPSN_LIGHTING)

        # Set OpenGL Clear Color
        SkyColor << options["sky color"]

        # Set fog settings
        if options["fog"]["enabled"]:
            fog_color = options["fog"]["color"]
            fog_start = options["fog"]["start"]
            fog_end   = options["fog"]["end"]

            Fog(fog_color, fog_start, fog_end)
    except Exception as e:
        _errcam = OrthographicCamera()
        _errwin = Window3D(camera=_errcam, width=512, height=240)
        Log.critical(f"{e}")

    # Start the engine
    engine.run()

    # Leave some space
    print()

    # Exit with no error
    return 0


# Program entry
if __name__ == "__main__":
    exit(main(list(sys.argv)))

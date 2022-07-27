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


from   capsian  import *
from   os      import system
import os
import sys
import json


def generate_capsian_config(project_name):
    return \
"""
{
    "sky color":  [0, 0, 0, 0],

    "lighting": {
        "enabled": true
    },

    "fog": {
        "enabled": false,
        "color": [0.5, 0.69, 1.0, 1.0],
        "start": 40,
        "end": 50
    },

    "camera": {
        "type": "perspective",

        "position": {
            "x": 0,
            "y": 0,
            "z": 0
        },

        "rotation": {
            "x": 0,
            "y": 0,
            "z": 0
        },

        "fov": 90,
        "far": 5000,
        "near": 0.05
    },

    "window": {
        "width": 800,
        "height": 600,
        "fullscreen": false,
        "vsync": false
    },

    "project": {
        "package": "__PROJECT__"
    }
}
""".replace("__PROJECT__", project_name)

def generate_script_template(projname, name):
    return \
f"""
# PROJECT: {projname}
# SCRIPT: {name}


from capsian import *
from addons import *


@IndependentComponent
class {name.capitalize()}Keyboard(KeyboardInputHandler):
    def on_key_press(self, symbol, modifiers):
        if symbol == Key.ENTER:
            print("Enter pressed")

    def on_key_released(self, symbol, modifiers) -> None:
        if symbol == Key.ENTER:
            print("Enter released")

    def on_key_held(self, keys: dict) -> None:
        if keys[Key.A]:
            print("A is held down")


@IndependentComponent
class {name.capitalize()}Mouse(MouseInputHandler):
    def on_button_press(self, x, y, button, modifiers) ->None:
        if button == MouseButton.LEFT:
            print("Left button pressed")

    def on_button_released(self, x, y, button, modifiers) -> None:
        if button == MouseButton.LEFT:
            print("Left button released")

    def on_button_held(self, buttons: dict) -> None:
        if buttons[MouseButton.LEFT]:
            print("Left button held down")


@IndependentComponent
class {name.capitalize()}(Script):
    def on_start(self, time) -> None:
        print("Hello world")

    def on_update(self, dt, time) -> None:
        print("Updated")

    def on_close(self, time) -> None:
        print("Closed")
"""


class Capsianline:
    @staticmethod
    def newproject(project_name="project"):
        if not os.path.exists(f"./{project_name}"):
            os.mkdir(f"./{project_name}")
            with open(f"./{project_name}/__init__.py", "w") as initfile:
                initfile.write(f"# Init file for project '{project_name}'")

            if not os.path.exists("./addons"):
                os.mkdir("./addons")

            if not os.path.exists("./capsian.json"):
                with open("./capsian.json", "w") as capconfig:
                    capconfig.write(generate_capsian_config(project_name))

                    Log.successful("Project created!")
                    return 0

            Log.successful("Project updated!")
            return 0
        
        Log.error("Project already exists")
        return -1

    @staticmethod
    def newscript(name):
        if not os.path.exists("./capsian.json"):
            Log.error("The current directory is not a valid Capsian Project")
            return -1

        with open("./capsian.json", "r") as preferences:
            configuration = json.loads(preferences.read())
            
            if "project" not in dict(configuration).keys():
                Log.error("Invalid Capsian Configuration File")
                return -2

            if "package" not in dict(configuration["project"]).keys():
                Log.error("Invalid Capsian Configuration File")
                return -3

            project_name = configuration["project"]["package"]
            if not os.path.exists(f"./{project_name}"):
                Log.warning("Project directory does not exist. About to create one...")
                Capsianline.newproject(project_name)

            with open(f"./{project_name}/{name}.py", "w") as script:
                script.write(generate_script_template(project_name, name))

            initfile_content = []
            with open(f"./{project_name}/__init__.py", "r") as initfile:
                initfile_content = initfile.readlines()

            with open(f"./{project_name}/__init__.py", "w") as initfile:
                initfile_content.append(f"\nimport {project_name}.{name}")
                initfile.writelines(initfile_content)

            Log.successful("Script created!")


# Main function
def main(argv: list) -> int:
    # Simple command
    if len(argv) >= 2 and hasattr(Capsianline, str(argv[1]).replace("--", "")):
        return getattr(Capsianline, str(argv[1]).replace("--", ""))(*argv[2:])

    if not os.path.exists("./capsian.json"):
        Log.error("Unable to locate Capsian Configuration File in working directory.")
        return -1

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

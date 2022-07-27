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


from   capsian.commands.project import ProjectCommand
from   capsian                  import *
import os
import sys
import json


class ScriptCommandSupportClass:
    @staticmethod
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



class ScriptCommand:
    @staticmethod
    def new(name="main"):
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
                ProjectCommand.new(project_name)

            with open(f"./{project_name}/{name}.py", "w") as script:
                script.write(ScriptCommandSupportClass.generate_script_template(project_name, name))

            initfile_content = []
            with open(f"./{project_name}/__init__.py", "r") as initfile:
                initfile_content = initfile.readlines()

            with open(f"./{project_name}/__init__.py", "w") as initfile:
                initfile_content.append(f"\nimport {project_name}.{name}")
                initfile.writelines(initfile_content)

            Log.successful("Script created!")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if hasattr(ScriptCommand, sys.argv[1]):
            getattr(ScriptCommand, sys.argv[1])(*sys.argv[2:])

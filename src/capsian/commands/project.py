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


from   capsian import *
import os
import sys


class ProjectCommandSupportClass:
    @staticmethod
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


class ProjectCommand:
    @staticmethod
    def new(project_name="project"):
        if not os.path.exists(f"./{project_name}"):
            os.mkdir(f"./{project_name}")
            with open(f"./{project_name}/__init__.py", "w") as initfile:
                initfile.write(f"# Init file for project '{project_name}'")

            if not os.path.exists("./addons"):
                os.mkdir("./addons")

            if not os.path.exists("./capsian.json"):
                with open("./capsian.json", "w") as capconfig:
                    capconfig.write(ProjectCommandSupportClass.generate_capsian_config(project_name))

                    Log.successful("Project created!")
                    return 0

            Log.successful("Project updated!")
            return 0
        
        Log.error("Project already exists")
        return -1


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if hasattr(ProjectCommand, sys.argv[1]):
            getattr(ProjectCommand, sys.argv[1])(*sys.argv[2:])

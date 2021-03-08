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
# Copyright 2020 - 2021 Alessandro Salerno (Tzyvoski)
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


from CapsianLine.commands.command import Command


class Package(Command):
    def __str__(self):
        return "package"


    def install(self, folder: str) -> None:
        import shutil
        
        with open(f"{folder}\\setup.json", "r") as setup:
            import json
            
            # load JSON
            try:
                from Capsian import Log
                Log.info(f"About to load setup file for package '{folder}'")
                global content, pkg_name, files
                content  = json.loads(setup.read())
                pkg_name = str(content["name"])
                files    = list(content["files"])
                Log.successful("Operation completed successfuly!")
            except:
                from Capsian import Log
                Log.error(f"Unable to load setup file for package '{folder}'")
                return

            # Create addon folder
            try:
                import os
                os.mkdir(f"addons\\{pkg_name}")
            except OSError as e:
                from Capsian import Log
                Log.error(f"Unable to create directory 'addons\\{pkg_name}'")
                return
            except Exception as e:
                raise e

            # Copy all files
            try:
                from   Capsian import Log
                import shutil

                for file in files:
                    target = f"addons\\{pkg_name}\\{file}"
                    origin = f"{folder}\\src\\{file}"
                    Log.info(f"About to load file {origin} and copy to {target}")
                    shutil.copyfile(origin, target)
                    Log.successful("Operation complete successfuly!")
                
                Log.successful("Copied all files!")
            except:
                from   Capsian import Log
                Log.error("Failed to copy files!")
                return

            with open("addons\\__init__.py", "w") as packages:
                for file in files:
                    packages.write(f"\nfrom addons.{pkg_name}.{file.replace('.py', '')} import *")

            from Capsian import Log
            Log.successful("Package fully installed!")

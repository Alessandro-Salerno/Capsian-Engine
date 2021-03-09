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
            import Capsian.engine as engine
            
            # load JSON
            try:
                from Capsian import Log
                Log.info(f"About to load setup file for package '{folder}'")
                global content, pkg_name, files, cpsn, ver, description
                content     = json.loads(setup.read())
                cpsn        = str(content["capsian"])
                ver         = str(content["version"])
                description = list(content["description"])
                pkg_name    = str(content["name"])
                files       = list(content["files"])
                Log.successful("Operation completed successfuly!")
            except:
                from Capsian import Log
                Log.error(f"Unable to load setup file for package '{folder}'")
                return

            if not cpsn == engine.version().replace("Capsian Engine v1.0 ", ""):
                from Capsian import Log
                Log.warning("This package is not compatible with your version of Capsian. Do you want to install it anyway?")
                ans = input(" [y/n] ")

                if ans == "n":
                    Log.info("Installation aborted!")
                    return

                elif ans == "y":
                    pass

                else:
                    Log.error("Invalid answer. Installation aborted!")
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

            with open(f"addons\\{pkg_name}\\__init__.py", "w") as packages:
                for file in files:
                    packages.write(f"\nfrom addons.{pkg_name}.{file.replace('.py', '')} import *")

            with open("addons\\__init__.py", "r") as packages:
                global lines
                lines = packages.readlines()

            with open("addons\\__init__.py", "w") as packages:
                lines.append(f"\nimport addons.{pkg_name} as {pkg_name}")
                packages.writelines(lines)

            pkg_info = json.dumps({
                "capsian": cpsn,
                "package": ver,
                "description": description
            })

            with open(f"addons\\{pkg_name}\\info.json", "w") as file:
                file.write(str(pkg_info))

            from Capsian import Log
            Log.successful("Package fully installed!")


    def list(self, output=True) -> list or None:
        import os
        _dirs = os.listdir("addons\\")
        dirs = []

        for _dir in _dirs:
            if os.path.isdir(f"addons\\{_dir}") and _dir:
                dirs.append(_dir)

        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        if not output:
            return dirs

        if len(dirs) == 0:
            print("No package installed")
            return

        for _dir in dirs:
            print(_dir)


    def uninstall(self, name: str) -> None:
        import shutil
        import os
        from   Capsian.log import Log

        if not name in self.list(False):
            from Capsian import Log
            Log.error(f"No such package '{name}'")
            return

        shutil.rmtree(f"addons\\{name}\\")

        with open("addons\\__init__.py", "r+") as imports:
            global lines
            lines = imports.readlines()

            for line in lines:
                if name in line:
                    lines.remove(line)

        with open("addons\\__init__.py", "w") as imports:
            imports.writelines(lines)

        Log.successful("Operation completed successfuly!")


    def info(self, name: str) -> None:
        import json
        from   Capsian import TermColor
        
        if not name in self.list(False):
            from Capsian import Log
            Log.error(f"No such package '{name}'")
            return

        with open(f"addons\\{name}\\info.json", "r") as info:
            content     = json.loads(info.read())
            cpsn        = content["capsian"]
            ver         = content["package"]
            description = content["description"]

            TermColor.begin(TermColor.OK_GREEN)
            print(f"Capsian Package {name}")
            TermColor.end()

            print(f"Made for Capsian {cpsn}")
            print(f"Package Version: {ver}")
            print()
            
            for row in description:
                print(row)

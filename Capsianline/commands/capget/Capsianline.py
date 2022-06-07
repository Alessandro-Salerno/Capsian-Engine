# ----------------------------------------------------------------------------
# Capsianline
# Copyright 2022 Carpal
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


import shutil
import Capsian
from Capsianline.commands.command import Command


class CapGet(Command):
    def __str__(self):
        return "capget"

    def __repr__(self) -> str:
        return f"""
{Capsian.TermColor.OK_GREEN}CAPGET{Capsian.TermColor.END_COLOR}
------
Capget is Capsian's new package manager.
The above-listed commands are all available and working!
"""


    def github(self, url: str, branch="master") -> None:
        import requests
        import zipfile
        import os
        import shutil
        
        try:
            Capsian.Log.info("About to download file...")
            req = requests.get(f"{url}//archive/refs/heads/{branch}.zip", allow_redirects=True)
            Capsian.Log.successful("Successfuly downloaded file!")

            Capsian.Log.info("About to store file...")
            with open("./addons/download.zip", "wb") as target:
                target.write(req.content)
            Capsian.Log.successful("Successfuly saved zip file!")

            Capsian.Log.info("About to unpack zip file...")
            with zipfile.ZipFile("./addons/download.zip", 'r') as zip_ref:
                zip_ref.extractall("./addons/download")
            Capsian.Log.successful("Successfuly unpacked zip file!")

            _dirs = os.listdir("./addons/download")

            for _dir in _dirs:
                if os.path.isdir(f"./addons/download/{_dir}"):
                    if os.path.exists(f"./addons/download/{_dir}/setup.json"):
                        self.install(f"./addons/download/{_dir}")
                    else:
                        dirs = os.listdir(f"./addons/download/{_dir}")
                        for dir in dirs:
                            if os.path.isdir(f"./addons/download/{_dir}/{dir}"):
                                self.install(f"./addons/download/{_dir}/{dir}")

            Capsian.Log.info ("About to dele all cache files...")
        except Exception as e:
            Capsian.Log.error(e)

        try:
            os.remove("./addons/download.zip")
            shutil.rmtree("./addons/download")
            Capsian.Log.successful("Successfuly deleted all cache files!")
        except:
            pass


    def install(self, folder: str) -> None:
        import shutil
        
        with open(f"{folder}/setup.json", "r") as setup:
            import json
            import os
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

                if os.path.exists(f"./addons/{pkg_name}"):
                    self.uninstall(pkg_name, False)

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
                    Log.info("Installation aborted.")
                    return

                elif ans == "y":
                    pass

                else:
                    Log.error("Invalid answer. Installation aborted!")
                    return

            # Create addon folder
            try:
                import os
                os.mkdir(f"addons/{pkg_name}")
            except OSError as e:
                from Capsian import Log
                Log.error(f"Unable to create directory 'addons/{pkg_name}'")
                return
            except Exception as e:
                raise e

            # Copy all files
            try:
                from   Capsian import Log
                import shutil

                for file in files:
                    target = f"addons/{pkg_name}/{file}"
                    origin = f"{folder}/src/{file}"
                    Log.info(f"About to load file {origin} and copy to {target}")
                    shutil.copyfile(origin, target)
                    Log.successful("Operation completed successfuly!")
                
                Log.successful("Copied all files!")
            except:
                from   Capsian import Log
                Log.error("Failed to copy files!")
                return

            with open(f"addons/{pkg_name}/__init__.py", "w") as packages:
                for file in files:
                    packages.write(f"\nfrom addons.{pkg_name}.{file.replace('.py', '')} import *")

            with open("addons/__init__.py", "r") as packages:
                global lines
                lines = packages.readlines()

            with open("addons/__init__.py", "w") as packages:
                lines.append(f"\nimport addons.{pkg_name} as {pkg_name}")
                packages.writelines(lines)

            pkg_info = json.dumps({
                "capsian": cpsn,
                "package": ver,
                "description": description
            })

            with open(f"addons/{pkg_name}/info.json", "w") as file:
                file.write(str(pkg_info))

            from Capsian import Log
            Log.successful("Package fully installed!")


    def list(self, output=True) -> list or None:
        import os
        _dirs = os.listdir("addons/")
        dirs = []

        for _dir in _dirs:
            if os.path.isdir(f"addons/{_dir}") and _dir:
                dirs.append(_dir)

        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        if not output:
            return dirs

        if len(dirs) == 0:
            print("No package installed")
            return

        print(f"{len(dirs)} package(s) installed\n")

        for _dir in dirs:
            print(f"-- {_dir}")


    def uninstall(self, name: str, output=True) -> None:
        import shutil
        import os
        from   Capsian.log import Log

        if not name in self.list(False):
            from Capsian import Log
            if output:
                Log.error(f"No such package '{name}'")
            
            return

        shutil.rmtree(f"addons/{name}/")

        with open("addons/__init__.py", "r+") as imports:
            global lines
            lines = imports.readlines()

            for line in lines:
                if name in line:
                    lines.remove(line)

        with open("addons/__init__.py", "w") as imports:
            imports.writelines(lines)

        if output:
            Log.successful("Operation completed successfuly!")


    def info(self, name: str) -> None:
        import json
        from   Capsian import TermColor
        
        if not name in self.list(False):
            from Capsian import Log
            Log.error(f"No such package '{name}'")
            return

        with open(f"addons/{name}/info.json", "r") as info:
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


    def reset(self):
        import shutil
        import os

        shutil.rmtree("./addons")
        os.mkdir("./addons")
        impts = open("./addons/__init__.py", "w")
        impts.close()
        Capsian.Log.successful("Operation completed successfuly!")


__linecommand__ = CapGet()

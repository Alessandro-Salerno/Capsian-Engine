# ----------------------------------------------------------------------------
# CapsianLine
# Copyright 2021 Carpal
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


from   CapsianLine.commands import *
from   CapsianLine.ccparser import *
import CapsianLine.design
import Capsian


# Draw the design for the header
CapsianLine.design.draw()

def get_package_list(dir: str):
   import os
   _dirs = os.listdir(dir)
   dirs = []

   for _dir in _dirs:
      if os.path.isdir(f"addons\\{_dir}") and _dir:
            dirs.append(_dir)

   if "__pycache__" in dirs:
      dirs.remove("__pycache__")

   return dirs


def command_exists(command: str):
   import json
   global jsfile

   with open("CapsianLine/paths.json", "r") as file:
      jsfile = json.loads(file.read())

   paths = jsfile["PATH"]

   for path in paths:
      try:
         file = open(f"{path}/{command}/capsianline.py", "r")
         file.close()
         return f"{path}/{command}/capsianline.py"
      except:
         continue

   return False


while True:
   try:
      # parse the command
      parser      = Parser(input(f"\n{Capsian.TermColor.FAIL}Capsian${Capsian.TermColor.WARNING} "))
      Capsian.TermColor.end()

      # get the tree
      tree        = parser.parse()
      
      # organize ..
      command     = tree[0] # .. the class
      sub_command = tree[1] # .. the method
      args        = tree[2] # .. the function args

      cmd_exists = command_exists(command)
      
      if cmd_exists == False:
         Capsian.Log.error(f"No such command \"{command}\"")
         continue
      
      __linecommand__ = None
      cmdcode = open(cmd_exists, "r")
      exec(compile(source=cmdcode.read(), filename="command", mode="exec"))

      if not hasattr(__linecommand__, sub_command):
         Capsian.Log.error(f"Command \"{command}\" has no subcommand \"{sub_command}\"")
         continue

      getattr(__linecommand__, sub_command)(*args)
      cmdcode.close()
   except KeyboardInterrupt:
      # catch ctrl + c
      print("\n\nTerminating program....")
      Capsian.TermColor.end()
      break

   except Exception as e:
      # some errors in the process? let's report it
      Capsian.Log.error(e)

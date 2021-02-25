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


# Imports
from   CapsianLine.commands import *
from   CapsianLine.ccparser import *
import CapsianLine.design
import Capsian


# Draw the design for the header
CapsianLine.design.draw()


while True:
   try:
      # parse the command
      parser      = Parser(input("\nCapsian$ "))

      # get the tree
      tree        = parser.parse()
      
      # organize ..
      command     = tree[0] # .. the class
      sub_command = tree[1] # .. the method
      args        = tree[2] # .. the function args

      # there isn't a key eq to command in the commands dictionary ?
      if not command in commands.keys():
         error(f"a class named {command} does not exist")

      # load the class from the dictionary
      entry      = commands[command]

      # there isn't a key eq to sub_command in entry ?
      # if not sub_command in entry.keys():
         # error(f"no declaration for a method named {sub_command} in the class {command}")
      
      # load the method from the class
      ptr = getattr(entry, sub_command)(*args)

   except KeyboardInterrupt:
      # catch ctrl + c
      print("system close")
      break

   except Exception as e:
      # some errors in the process? let's report it
      Capsian.Log.error(e)

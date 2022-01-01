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


from Capsian import *

# Init the program
import os
os.system("cls" if os.name == "nt" else "clear")


def draw():
    print("============================================================================")
    TermColor.begin(TermColor.OK_BLUE)
    print(f"Capsianline v2.0 for {engine.version()}")
    print("Capsian: https://github.com/tzyvoski/Capsian-Engine")
    print("Capsianline: https://github.com/Carpall/Capsianline", end="\n")
    TermColor.end()

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
# KeyFire Engine
# Copyright 2019 - 2020 Alessandro Salerno (Tzyvoski)
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
from locals import *
from os import system
import tzylang as translate
import sys
import time
import os


# List of all commands
cmds = [
    "1. commands - Shows this",
    "2. parse - Translates your TzyLang code in Python and prints it",
    "3. run - Translates and runs your TzyLang code",
    "4. clear - Resets the console to it's original state",
    "5. system('command') - Runs the specified command as you were running it in the command prompt",
    "6. tzylang - Sets the console i n TzyLang mode",
    "7. modules - shows all the modules that are pre-imported by the console",
    "8. Most python commands (Such as import)"
]


imports = [
    "KeyFire (locals.py)",
    "os.system (system)",
    "os",
    "translate (tzylang.py)",
    "sys",
    "time"
]


def run(mode=KFE_NORMAL_MODE):
    with open("scripts/script.kfel", 'r') as file:
        lines = file.readlines()
        exec(compile(source=mode, filename="", mode="exec", optimize=1))

    system("main.py") if os.name == "nt" else system("python3 main.py")


def commands():
    out(f"{TermColor.OK_BLUE}{TermColor.BOLD} **List of all commands** {TermColor.OK_GREEN}")

    for command in cmds:
        out(command)

    out(f"{TermColor.END_COLOR}")


def parse():
    with open("scripts/script.kfel", 'r') as file:
        global source
        source = translate.build(file.read())

    print(source)


def out(text, end="\n"):
    print(text, end=end)


def clear():
    system("cls") if os.name == "nt" else system("clear")

    print(
        f"{TermColor.WARNING}Copyright 2019 - 2020 Alessandro Salerno (Tzyvoski)\nLICENSE: http://www.apache.org/licenses/LICENSE-2.0\nKeyFire Console 0.2 for KeyFire 2.1 beta 6 preview 1\n{TermColor.END_COLOR}")


def tzylang():
    while True:
        out(f"{TermColor.OK_GREEN}TzyLang/KeyFire{TermColor.FAIL}${TermColor.END_COLOR} ", end=" ")
        tzy_cmd = input()

        try:
            try:
                exec(compile(source=translate.buid(tzy_cmd), filename="tzy_command", mode="exec", optimize=1))
            except:
                Log.error("The command you specified is not valid")
        except:
            pass


# Lists all the available modules
def modules():
    for module in imports:
        out(module)


# When the program starts
clear()
print()
commands()


# Main loop
while True:
    out(f"{TermColor.OK_GREEN}Python/KeyFire{TermColor.FAIL}${TermColor.END_COLOR} ", end=" ")
    cmd = input()

    try:
        new_code = cmd + "()"
        exec(compile(source=new_code, filename="command", mode="exec", optimize=1))
    except:
        try:
            exec(compile(source=cmd, filename="command", mode="exec", optimize=1))
        except:
            Log.error("The command you specified is not valid")

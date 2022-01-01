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
#  * Redistributioans of source code must retain the above copyright
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


from Capsian.components.component import Component


class Transform(Component):
    """
    A Transform is a component that holds date about the position, rotation and size of an object.
    It is a standalone component in order to allow for the existance of EmptyObjects with no location, useful
    for things like KeyboardInputHandler components that don't need any position, but just an entity to update them. 

    Fields
    ------
        x      | The transform's X position  | float
        y      | The transforms's Y position | float
        z      | The transform's Z position  | float
        width  | The transform's width       | float
        height | The transform's height      | float
        depth  | The transform's depth       | float
        rotX   | The transofrm's X rotation  | float
        rotY   | The transform's Y rotation  | float
        rotZ   | The transform's Z rotation  | float
        dx     | The transform's X direction | float
        dy     | The transform's Y direction | float
        dz     | The transform's Z rotation  | float

    Properties
    ----------
        position  | The transform's position  | list [x, y, z]
        size      | The transform's size      | list [width, height, depth]
        rotation  | The transform's rotation  | list [rotX, rotY, rotZ]
        direction | The transform's direction | list [dx, dy, dz]
    """

    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, x=0, y=0, z=0, width=1, height=1, depth=1, rotX=0, rotY=0, rotZ=0, dx=0, dy=0, dz=0):
        self.x        =  float(x)
        self.y        =  float(y)
        self.z        =  float(z)

        self.width    =  width
        self.height   =  height
        self.depth    =  depth

        self.rotX     =  float(rotX)
        self.rotY     =  float(rotY)
        self.rotZ     =  float(rotZ)

        self.dx       = float(dx)
        self.dy       = float(dy)
        self.dz       = float(dz)

        super().__init__()


    def __repr__(self):
        return "transform"


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    @property
    def position(self) -> list:
        return [self.x, self.y, self.z]


    @property
    def size(self) -> list:
        return [self.width, self.height, self.depth]

    
    @property
    def rotation(self) -> list:
        return [self.rotX, self.rotY, self.rotZ]


    @property
    def direction(self) -> list:
        return [self.dx, self.dy, self.dz]

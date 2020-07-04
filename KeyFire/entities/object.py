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


from locals import *


class Object:
    """
    A generic KeyFire object

    """

    def __init__(self, size=[1, 1, 1], pos=[0, 0, 0], rot=[0, 0, 0], batch=None):
        """
        Creates an object in the world
        This is usually used as super/parent class for other objects like Cubes

        :param size: The size of the object (Array, [width, height, depth])
        :param pos: The position of the world in 3 Space (Array, [x, y, z])
        :param rot: The rotation of the object (Array, [x, y])
        :param batch: The scene in which the object should be rendered
        """

        self.size = size
        self.pos = pos
        self.rot = rot
        self.batch = batch
        graphics.stack.append(self)


    # Rotate using glRotatef()
    def rotate(self, X, Y, Z):
        """
        Doesn't work
        USELESS

        :param X:
        :param Y:
        :param Z:
        :return:
        """

        OpenGL.glRotatef(self.rot, X, Y, Z)


    # Update (Ovveride this)
    def update(self, delta_time):
        """
        Updates the object.
        This is never automatically called, you CAN call this yourself from your update function

        :param delta_time: The delta time of the loop
        :return: Nothing
        """

        pass


    # Overridable method
    def override_me(self, *args):
        """
        This method is empty on purpose.
        It does nothing, but you can override this to make it do something!

        :param args:All the arguments you want
        :return: Whatever you want
        """

        pass


    # Start timer
    def start_loop(self):
        """
        Starts the loop
        Call this just once

        :return: Nothing
        """

        Framework.clock.schedule_interval(self.update, 1/120)


    # Draw object
    def draw(self):
        """
        Draws the object

        :return: Nothing
        """

        self.batch.draw()

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
# Copyright 2020 Alessandro Salerno (Tzyvoski)
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



from   locals                  import *
import random
from   Capsian.entities.square import Square


class Particle:
    def __init__(self, pos=[0, 0, 0], quantity=1, direction=[0, -0.01, 0], size=[0.25, 0.25, 0.25], lifetime=240):
        self.pos       = pos
        self.quantity  = quantity
        self.lifetime  = lifetime
        self.dead      = 0
        self.quads     = []
        self.size      = size
        self.direction = direction

        graphics.stack.append(self)


    # Move the particle
    def move(self, dx, dy, dz):
        for quad in self.quads:
            quad.pos[0] += dx
            quad.pos[1] -= dy
            quad.pos[2] += dz


#####################################################################################################################################################################################################################################################################


class Particles2D(Particle):
    """
    Particles are 2D objects rendered in a 3D scene.
    They can move in a specific direction and disappear once their lifetime expires.
    NOTE: They may have a big impact on your game's performance. This will be fixed in a later version

    """

    def __init__(self, pos=[0, 0, 0], quantity=1, direction=[0, -0.01, 0], size=[0.25, 0.25, 0.25], lifetime=240):
        """
        Creates particles in the world

        :param pos: Position in 3D space (Array, [x, y, z])
        :param quantity: How many particles should spawn every time the create() function is called (Int)
        :param direction: The direction in which the particles should move (Array, [dx, dy, dz])
        :param size: The size of a single particle (Array, [length, height]
        :param lifetime: How long a particles should last - Expressed in ticks (1Tick = 1/120 sec) - (Int)
        """

        super().__init__(pos, quantity, direction, size, lifetime)

        self.create(quantity=quantity, pos=[self.pos[0], self.pos[1], self.pos[2]])


    # Kill function
    def kill(self):
        """
        Kills a given particle.
        This is automatically called after the lifetime expires

        :return: Nothing
        """

        self.dead = 0
        Framework.clock.unschedule(self.check)

        for quad in self.quads:
            quad.delete()

        del self


    # Check function
    def check(self, delta_time):
        """
        This method checks if the particle should be killed
        This is automatically called every tick

        :param delta_time: Float (1/120)
        :return: Nothing
        """

        if self.dead < self.lifetime:
            self.dead += 1
            self.move(dx=self.direction[0], dy=self.direction[1], dz=self.direction[2])
        else:
            self.kill()


    # Create particles
    def create(self, quantity, pos):
        """
        This method creates the particles.
        You can call this, but there's not reason to as it's automatically called by the constructor

        :param quantity: Int
        :param pos: Array [x, y, z]
        :return: Nothing
        """

        for _ in range(0, quantity):
            x = pos[0] + random.uniform(-self.size[0] * 2, self.size[2] * 2)
            y = pos[1] + random.uniform(-self.size[0], self.size[2] / 2)
            z = pos[2] + random.uniform(self.size[0] * 2, self.size[2] * 2)

            p = Square(color=None, size=self.size, pos=[x, y, z], rot=[0, 0])
            p.set_flag("look_at_camera", True)
            self.quads.append(p)

        Framework.clock.schedule_interval(self.check, 1/120)


#####################################################################################################################################################################################################################################################################


class ParticleBatch(Particle):
    def __init__(self, quantity=1, pos=[[0, 0, 0]], size=[[0.25, 0.25, 0.25]], direction=[0, -0.01, 0], lifetime=240):
        """
        Creates a particle batch in the world.
        This is like normal particles, except it may limit you in some way.
        This may also improve performance compared to normal particles.

        :param quantity: How many particles should be part of the batch (Int)
        :param pos: The position of each particle in the world (Array of arrays [[x, y, z], [x, y z]]...)
        :param size: The size of a particle (Array [length, height])
        :param direction: The direction in which all the particles in a batch will move (Array [dx, dy, dz])
        :param lifetime: The lifetime of all the particles in a batch
        """

        super().__init__(pos=pos, quantity=quantity, direction=direction, size=size, lifetime=lifetime)

        for _ in range(0, len(pos)):
            self.create(quantity=quantity, pos=pos[_], size=size[_])


    # Kill function
    def kill(self):
        """
        Kills a given particle.
        This is automatically called after the lifetime expires

        :return: Nothing
        """

        self.dead = 0
        Framework.clock.unschedule(self.check)

        for quad in self.quads:
            quad.delete()

        del self


    # Check function
    def check(self, delta_time):
        """
        This method checks if the particle should be killed
        This is automatically called every tick

        :param delta_time: 1 tick (1/120 sec)
        :return: Nothing
        """

        if self.dead < self.lifetime:
            self.dead += 1
            self.move(dx=self.direction[0], dy=self.direction[1], dz=self.direction[2])
        else:
            self.kill()


    # Create particles
    def create(self, quantity, pos, size):
        """
        This method creates the particles.
        You can call this, but there's not reason to as it's automatically called by the constructor

        :param quantity: Ho many particles should be in each particle subset
        :param pos: The position of a single particle
        :return: Nothing
        """

        for _ in range(0, quantity):
            x = pos[0] + random.uniform(-size[0] * 2, size[2] * 2)
            y = pos[1] + random.uniform(-size[0], size[2] / 2)
            z = pos[2] + random.uniform(size[0] * 2, size[2] * 2)

            p = Square(color=None, size=size, pos=[x, y, z], rot=[0, 0])
            p.set_flag("look_at_camera", True)
            self.quads.append(p)

        Framework.clock.schedule_interval(self.check, 1/120)

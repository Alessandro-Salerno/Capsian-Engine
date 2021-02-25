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


from   Capsian.entities.entity   import Entity
from   Capsian.entities.square import RotatingSquare
import Capsian.engine          as engine
import pyglet
import random


class Particle(Entity):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=None, amount=4, duration=240, scene=None):
        """
        Creates a Particle derivative (Such as Particles2D)

        :param transform: A Transform object
        :param amount: Amount of particles to be generated (Int)
        :param duration: The duration of the particle
        :param scene: A Scene object
        """

        super().__init__(
            transform,
            scene,
            True
        )

        self.dead      = 0
        self.quads     = list()
        self.amount    = int(amount)
        self.duration  = float(duration)

        self.create(
            amount,
            self.components.transform.position,
            self.components.transform.size
        )


    # Move the particle
    def move(self, dx, dy, dz, dt):
        for quad in self.quads:
            quad.components.transform.x += dx * dt
            quad.components.transform.y += dy * dt
            quad.components.transform.z += dz * dt


#####################################################################################################################################################################################################################################################################


class Particles2D(Particle):
    """
    Particles are 2D objects rendered in a 3D scene.
    They can move in a specific direction and disappear once their lifetime expires.
    NOTE: They may have a big impact on your game's performance. This will be fixed in a later version
    """

    # Kill function
    def kill(self):
        """
        Kills a given particle.
        This is automatically called after the lifetime expires

        :return: None
        """

        self.dead = 0
        pyglet.clock.unschedule(self.check)
        pyglet.clock.unschedule(self.destroy)

        for quad in self.quads:
            quad.delete()

        del self


    # Check function
    def check(self, dt):
        """
        This method checks if the particle should be killed
        This is automatically called every tick

        :param delta_time: Float (1/120)
        :return: None
        """

        if not self.dead < self.duration:
            self.kill()

        self.move(
            dx=self.components.transform.dx,
            dy=self.components.transform.dy,
            dz=self.components.transform.dz,
            dt=dt
        )


    # Create particles
    def create(self, quantity, pos, size):
        """
        This method creates the particles.
        You can call this, but there's not reason to as it's automatically called by the constructor

        :param quantity: Int
        :param pos: Array [x, y, z]
        :return: None
        """

        from Capsian import Transform

        for _ in range(quantity):
            x = pos[0] + random.uniform(-size[0] * 2,  size[2] * 2)
            y = pos[1] + random.uniform(-size[0]    ,  size[2] / 2)
            z = pos[2] + random.uniform( size[0] * 2,  size[2] * 2)

            p = RotatingSquare(
                Transform(
                    x, y, z,
                    size[0], size[1], size[2]
                ),
                self.scene,
                False
            )

            self.quads.append(p)

        engine.default_clock.Schedule.call_every_tick(self.check)
        engine.default_clock.Schedule.call_with_interval(self.destroy, 1)


    def destroy(self, dt):
        if self.dead < self.duration:
            self.dead += 1


#####################################################################################################################################################################################################################################################################


class ParticleBatch(Particle):
    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------
    
    def __init__(self, transform=None, amount=1, duration=240, scene=None):
        """
        Creates a particle batch in the world.
        This is like normal particles, except it may limit you in some way.
        NOTE: This may have better performance 

        :param transform: A Transform object
        :param amount: Amount of particles to be generated (Int)
        :param duration: The duration of the particle
        :param scene: A Scene object
        """

        super().__init__(
            transform=transform,
            amount=amount,
            duration=duration,
            scene=scene
        )

        for _ in range(0, len(pos)):
            self.create(quantity=quantity, pos=pos[_], size=size[_])


    # Kill function
    def kill(self):
        """
        Kills a given particle.
        This is automatically called after the lifetime expires

        :return: None
        """

        self.dead = 0
        pyglet.clock.unschedule(self.check)

        for quad in self.quads:
            quad.delete()

        del self


    # Check function
    def check(self, dt):
        """
        This method checks if the particle should be killed
        This is automatically called every tick

        :param delta_time: 1 tick (1/120 sec)
        :return: None
        """

        if self.dead < self.lifetime:
            self.kill()

        self.dead += 1

        self.move(
            dx=self.components.transform.dx,
            dy=self.components.transform.dy,
            dz=self.components.transform.dz,
            dt=dt
        )


    # Create particles
    def create(self, quantity, pos, size):
        """
        This method creates the particles.
        You can call this, but there's not reason to as it's automatically called by the constructor

        :param quantity: Ho many particles should be in each particle subset
        :param pos: The position of a single particle
        :return: None
        """

        from Capsian import Transform

        for _ in range(quantity):
            x = pos[0] + random.uniform(-size[0] * 2, size[2] * 2)
            y = pos[1] + random.uniform(-size[0]    , size[2] / 2)
            z = pos[2] + random.uniform(size[0] *  2, size[2] * 2)

            p = RotatingSquare(
                Transform(
                    x, y, z,
                    size[0], size[1], size[2]
                ),
                self.scene,
                False
            )

            self.quads.append(p)

        engine.default_clock.Schedule.call_with_interval(self.check, 1/120)

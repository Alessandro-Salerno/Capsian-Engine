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


from   Capsian.entities.entity      import Entity
from   Capsian.components.transform import Transform
from   Capsian.entities.square      import RotatingSquare
import Capsian.engine               as     engine
import pyglet
import random


class Particle(Entity):
    """
    Fields
    ------
        dead     | The timer for the destruction                                       | int
        quads    | The lsit of quads that are currently being rendered in the Particle | list [Square]
        amount   | The amount of quads in the Particle                                 | int
        duration | The duration of the effect                                          | float

    Methods
    -------
        move | Moves the particles in the designated direction
    """

    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self, transform=Transform(), amount=4, duration=240, scene=None):
        """
        Parameters
        ----------
            transform | A Capsian Transform Object                           | Transform
            amount    | The amount of particles to be generated              | int
            duration  | The duration of the effect                           | int
            scene     | The Capsian Scene of which the particles are part of | Scene3D
        """

        super().__init__(
            transform,
            scene,
            False
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
    def move(self, dx: float, dy: float, dz: float, dt: float) -> None:
        for quad in self.quads:
            quad.components.transform.x += dx * dt
            quad.components.transform.y += dy * dt
            quad.components.transform.z += dz * dt


#####################################################################################################################################################################################################################################################################


class Particles3D(Particle):
    """
    Methods
    -------
        kill    | kills all the quds in the particle
        check   | Checks the state of all a quad in the particle
        create  | Creates the particles
        destroy | Destroyes the object
    """


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    # Kill function
    def kill(self) -> None:
        self.dead = 0
        pyglet.clock.unschedule(self.check)
        pyglet.clock.unschedule(self.destroy)

        for quad in self.quads:
            quad.delete()

        del self


    # Check function
    def check(self, dt: float) -> None:
        if not self.dead < self.duration:
            self.kill()

        self.move(
            dx=self.components.transform.dx,
            dy=self.components.transform.dy,
            dz=self.components.transform.dz,
            dt=dt
        )


    # Create particles
    def create(self, quantity: int, pos: list, size: list) -> None:
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


    def destroy(self, dt: float) -> None:
        if self.dead < self.duration:
            self.dead += 1

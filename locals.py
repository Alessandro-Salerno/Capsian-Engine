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
# Copyright (c) 2019 - 2020 Alessandro Salerno (Tzyvoski)
# All rights reserved.
#
# Redistribution of the engine (In source or binary form) is allowed provided
# that the following requirements are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistribution in binary form must contain all scripts (Such as script.kfel)
#
#
# **DISCLAIMER**
#
# KEYFIRE AND IT'S CREATOR ARE NOT RESPONSIBLE FOR THE USE DEVELOPERS MAE OF
# THE ENGINE.
# ----------------------------------------------------------------------------


import pyglet                         as     Framework
import pyglet.gl                      as     OpenGL
import pyglet.window.key              as     Key
from KeyFire.values                   import *

from KeyFire.world.format             import *
from KeyFire.log                      import Log
import KeyFire.engine                 as     engine
import KeyFire.video.graphics         as     graphics
from KeyFire.entities.object          import Object
from KeyFire.video.window             import Window3D
from KeyFire.video.camera             import PerspectiveCamera
from KeyFire.video.camera             import OrthographicCamera
from KeyFire.video.scene              import Scene
from KeyFire.entities.cube            import Cube
from KeyFire.texturing.material       import Material
from KeyFire.input.keyboard           import KeyboardInputHandler
from KeyFire.entities.particle_system import Particles2D
from KeyFire.entities.particle_system import Particle
from KeyFire.entities.particle_system import ParticleBatch
from KeyFire.entities.square          import Square
from KeyFire.audio.music              import Track
from KeyFire.audio.sound              import DirectionalSound
from KeyFire.texturing.texture        import Texture3D
from KeyFire.texturing.texture        import SmartTexture3D
from KeyFire.GUI.label                import StaticLabel2D
from KeyFire.GUI.label                import StaticLabel3D
from KeyFire.GUI.label                import DynamicLabel3D
from KeyFire.video.light              import Light3D
from KeyFire.video.light              import AmbientLight
from KeyFire.log                      import TermColor
from KeyFire.GUI.sprite               import DynamicSprite3D
from KeyFire.texturing.texture        import Texture2D
from KeyFire.entities.square          import TexturedSquare
from KeyFire.texturing.texture        import Image2D
from KeyFire.video.fps_counter        import FPSCounter
from KeyFire.video.fog                import Fog
import KeyFire.maths.math             as     kmath

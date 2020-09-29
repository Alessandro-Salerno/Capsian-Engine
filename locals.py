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
# Copyright (c) 2020 Alessandro Salerno (Tzyvoski)
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
# Capsian AND IT'S CREATOR ARE NOT RESPONSIBLE FOR THE USE DEVELOPERS MAE OF
# THE ENGINE.
# ----------------------------------------------------------------------------


import lib.pyglet                         as     Framework
import lib.pyglet.gl                      as     OpenGL
import lib.pyglet.window.key              as     Key
from Capsian.values                       import *

from Capsian.world.format                 import *
from Capsian.log                          import Log
import Capsian.engine                     as     engine
import Capsian.video.sky_color            as     sky_color
from Capsian.entities.object              import Object
from Capsian.video.window                 import Window3D
from Capsian.video.camera                 import PerspectiveCamera
from Capsian.video.camera                 import OrthographicCamera
from Capsian.video.scene                  import Scene
from Capsian.entities.cube                import Cube
from Capsian.texturing.material           import Material
from Capsian.input.keyboard               import KeyboardInputHandler
from Capsian.entities.particle_system     import Particles2D
from Capsian.entities.particle_system     import Particle
from Capsian.entities.particle_system     import ParticleBatch
from Capsian.entities.square              import Square
from Capsian.audio.music                  import Track
from Capsian.audio.sound                  import DirectionalSound
from Capsian.texturing.texture            import Texture3D
from Capsian.texturing.texture            import SmartTexture3D
from Capsian.GUI.label                    import StaticLabel2D
from Capsian.GUI.label                    import StaticLabel3D
from Capsian.GUI.label                    import DynamicLabel3D
from Capsian.video.light                  import Light3D
from Capsian.video.light                  import AmbientLight
from Capsian.log                          import TermColor
from Capsian.GUI.sprite                   import DynamicSprite3D
from Capsian.texturing.texture            import Texture2D
from Capsian.entities.square              import TexturedSquare
from Capsian.texturing.texture            import Image2D
from Capsian.video.fps_counter            import FPSCounter
from Capsian.video.fog                    import Fog
import Capsian.maths.math                 as     kmath

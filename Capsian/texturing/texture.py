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


from locals import *


class Texture:
    def __init__(self, file, texture_type, flags=types.FlagList([types.Flag("texture mode", CPSN_DEFAULT_TEXTURE_MODE)])):
        """
        Defines a texture object that can then be used with a material.
        It loads all pixels in a given image file

        :param file: The file path from which the system should load the texture (String)
        :param flags: Flags for loading th texture (Dict, {"texture_mode": CPSN_DEFAULT_TEXTURE_MODE or Array [GL_FILTER1, GL_FILTER2, GL_TEXTURE_TARGET})
        """
        
        self.path  = file
        self.flags = flags


########################################################################################################################


class Texture3D(Texture):
    def __init__(self, file, flags=types.FlagList([types.Flag("texture mode", CPSN_DEFAULT_TEXTURE_MODE)])):
        super().__init__(file, "texture3D", flags)


    # Get the texture group
    def get_texture(self):
        file = self.path

        try:
            loaded_texture = Framework.image.load(file).get_texture()

            Framework.gl.glTexParameterf(
                Framework.gl.GL_TEXTURE_2D,
                self.flags["texture mode"][0], self.flags["texture mode"][2]
            )

            Framework.gl.glTexParameterf(
                Framework.gl.GL_TEXTURE_2D,
                self.flags["texture mode"][1], self.flags["texture mode"][2]
            )

            Log.successful(f"Successfully loaded texture from file '{file}'")
            return Framework.graphics.TextureGroup(loaded_texture)
        except Exception as exception:
            Log.critical(f"Unable to load texture from file '{file}'. Check the file name and the material's flags!\n\n{exception}")


########################################################################################################################


class SmartTexture3D(Texture):
    def __init__(self, file, transform, flags=types.FlagList([types.Flag("texture mode", CPSN_DEFAULT_TEXTURE_MODE)])):
        """
        Creates a texture object that can by used with a matrial
        This won't load all pixels in a given image file, but will load all pixels in a specific area of an image file

        :param file:
        :param coords: The coordinates from which the texture starts in the file (Array, [x, y])
        :param size: The size of the region from which the system should load the texture file (Array, [length, height])
        :param flags: Flags for loading th texture (Dict, {"texture_mode": CPSN_DEFAULT_TEXTURE_MODE or Array [GL_FILTER1, GL_FILTER2, GL_TEXTURE_TARGET})
        """

        super().__init__(file=file, texture_type="smartTexture3D", flags=flags)
        self.pos  = transform.position
        self.size = transform.size


    def get_texture(self):
        try:
            loaded_texture = Framework.image.load(self.path).get_region(
                self.pos[0],
                self.pos[1],
                self.size[0],
                self.size[1]
            ).get_texture()
            
            Framework.gl.glTexParameterf(
                Framework.gl.GL_TEXTURE_2D,
                self.flags["texture mode"][0], self.flags["texture mode"][2]
            )

            Framework.gl.glTexParameterf(
                Framework.gl.GL_TEXTURE_2D,
                self.flags["texture mode"][1], self.flags["texture mode"][2]
            )

            Log.successful(f"Successfully loaded texture from file '{self.path}'")
            return Framework.graphics.TextureGroup(loaded_texture)
        except:
            Log.critical(f"Unable to load texture from file '{self.path}'. Check the file name and the material's flags!")


########################################################################################################################


class Image2D:
    def __init__(self, file):
        self.path  = file
        self.image = self.get_image()


    def get_image(self):
        file = self.path

        try:
            loaded_texture = Framework.image.load(file)
            Log.successful(f"Successfully loaded texture from file '{file}'")
            return loaded_texture
        except:
            Log.critical("Unable to load texture from file '{file}'. Check the file name and the material's flags!")

    
    def get_texture(self):
        return self.image.get_texture()

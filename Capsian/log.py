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



from datetime import datetime
from locals import *
from os import system
import sys


class TermColor:
    """
    Gives colors for the Terminal/Command Prompt

    """

    HEADER    = '\033[95m'
    OK_BLUE   = '\033[94m'
    OK_GREEN  = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    END_COLOR = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


# Returns the time and date
def time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


class Log:
    """
    Logs the engine's activity.
    You can also use this in your Capsian applications if you need to

    """

    # Print error
    @staticmethod
    def error(text):
        """
        Displays an error.
        This comes in the form of console output

        :param text: The error's text
        :return: Nothing
        """

        print(
            f"{TermColor.FAIL} [{time()} ERROR] {text} {TermColor.END_COLOR}"
        )

    # Critical function
    @staticmethod
    def critical(text):
        """
        Shows an error message.
        This message may come in different forms: It may be a graphical one, or a console based one depending on your
        application's specs.

        :param text: The text that is displayed
        :return: Nothing
        """

        try:
            # Load all necessary libs
            from os import system
            from locals import engine
            from locals import Scene
            from Capsian.values import SkyColor
            from locals import OrthographicCamera

            engine.main_window.set_fullscreen(False)

            # Prepare window
            camera = OrthographicCamera()

            # Setup the Window
            SkyColor << [0.0, 0.0, 0.0, 1.0]
            engine.main_window.set_viewport(camera)   

            engine.main_window.set_caption("Capsian 1.0 - UNSTABLE STATE")

            # Print the error to the console
            print(f"{TermColor.FAIL} [{time()} FATAL ERROR] {text} {TermColor.END_COLOR}")

            # Draw the message
            error_scene = Scene(camera, CPSN_GUI_SCENE)


            error = Framework.text.Label(
                text=f"{text}\n\nPress ENTER or ESCAPE to terminate the execution of the program.\n_",
                font_name="consolas", font_size=24, bold=True,
                width=engine.main_window.width - 25, italic=False,
                x=10, y=engine.main_window.height,
                anchor_x="left", anchor_y="top",
                batch=error_scene.batch, multiline=True)
        except:
            print(f"{TermColor.FAIL} [{time()} FATAL ERROR] {text} {TermColor.END_COLOR}")

        try:
            from locals import engine
            engine.main_window.alive = 0
        except:
            pass


    # Warning function
    @staticmethod
    def warning(text):
        """
        Displays a warning in the console

        :param text: The warning's text
        :return: Nothing
        """

        print(
            f"{TermColor.WARNING} [{time()} WARNING] {text} {TermColor.END_COLOR}"
        )


    # Information function
    @staticmethod
    def info(text):
        """
        Displays information in the console

        :param text: The text that should be displayed
        :return: Nothing
        """

        print(
            f"{TermColor.BOLD} [{time()} INFO] {text} {TermColor.END_COLOR}"
        )


    # Successful function
    @staticmethod
    def successful(text):
        """
        Displays a successful message.
        This is used to tell the user if something worked.

        :param text: The text that should be printed to the console
        :return: Nothing
        """

        print(
            f"{TermColor.OK_GREEN} [{time()} SUCCESSFUL] {text} {TermColor.END_COLOR}"
        )

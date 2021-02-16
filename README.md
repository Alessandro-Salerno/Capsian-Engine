# Overview
Capsian is a weird, incomplete and performant Python game engine.
The project was initially named "KeyFire Engine" but was later renaemd to Capsian due to trademark related issues.

# Performance
The latest version of Capsian brings with it numerous improvementss to performance.
Previous versions struggled to handle over 500 non-batched objects in a scene. This version, though, with the new clock and ticking mechanics, pushes performance to the sky: with an averege of 2000 FPS at 5120x2880 and 4700FPS at 1280x720. You can read the code in files "Capsian/video/scene.py" , "Capsian/video/window.py" and "Capsian/world/clock.py" to find out what makes it so performant. 

ALL TESTS WERE CONDUCTED ON A GTX 1080 AND INTEL CORE i7 8700K 3.70GHz

# Languages
Capsian uses Python as both its scripting language and its source language (TCL, C, C++ and the others you see on the right come from libs and the venv).
Until a while ago, there was also support for a custom parsed language called "tzylang", but it's since been removed due to parsing related issues. 
Other scripting languages will probably be added in the futures (C# Being my main focus), but for now this is what you get

# Requirements
Capsian now incldues a Python Virtual Enviroment (venv) to insure everybody has the same experience, regardless of what they have installed on their machine.
This doesn't mean, though, that there's nothing you need or may want to do to improve your coding experience
- Windows 10
- Microsoft Visual Studio Code with alle necessary extensions

Unfortunatelly I don't have a Linux machine (And not even a VM right now) which prevents me from creating a Linux venv, thus worsening your coding experience on Linux.
This doesn't mean you can't use Capsian on Linux though. Yuo can, it's just that you'll have to install pyglet 1.5.6 and Python 3.7.3 on your machine 

Visual Studio Code is a great editor as it doesn't force you to use your machine's Python Interpreter, but allows you to choose it. Read the next block for more information

# Setting up VS Code for Capsian
In the bottom-left of the VS Code window, you should see a few buttons
1. Make sure you have the Python extension installed
2. Select your python interpreter (Recommended: Python/Windows/python.exe)
3. Always run your app rith the "WinRuntime.bat" file!

# Older versions
You can find all older versions of Capsian (KeyFire) at: https://tzyvoski.wixsite.com/keyfire

# Myself
I am ALessandro Salerno, AKA tzyvoski. I was born in Italy and I still live there. And yes, I love Pizza 😂
I study IT in high school and have been working on Capsian (And its predecessors) for one and a half years. 

# Commits and branching
Please do NOT commit and push to the master branch, you can clone the repository or create another branch as stated by the license in the LICENSE.txt file
If you think your contributions could help a lot, then write to my email address (miro.salerno@icloud.com). I amy or may not accept the contribution and implement it in the engine directly. IN this case, you'll be listed in the credits

# Credits
All though I am the solo developer of Capsian, some people helped me and still help me, here are some of them
- Carpal (From the Italian Discord Server "Tecnologia Per Tutt") [CapsianLine https://github.com/Carpall/capsianline]
- Liam (From the Italian Discord Server "Tecnologia per Tutti")
- Lorenzo Bergadano (From Real life 😂)
- Pyglet and the pyglet contributors for providing the amazing toolkit used to make Capsian
- Me, of course 💹🤣

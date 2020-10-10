# Overview
Capsian is a weird, incomplete and performant Python game engine.
It was initially called "KeyFire Engine" but it was later renaemd to apsian due to trademark related issues.

# Performance
Capsian's performance are pretty great. All though written in Python, the engine's performance ae good at worst and amazing at best.
While testing, the highest framerate recorded was 169000 FPS, to make clear just how much this is, if you rendered exactly 60 frames per second, it would take you 46 minutes to ssee a simular amount of frames.
There are ares of the engine, such as 2D, that could be improved both in features and in performance, but overall you are not gonna have big performance problems. 
Newer tests, though, performed on Capsian (Commit f510490), reveal slitelly lower highs but much metter overall performance, with much more stable framerate avereging in the 2000's

ALL TESTS WERE CONDUCTED ON A GTX 1080 AND INTEL CORE i7 8700K 3.70GHz

# Languages
Capsian uses Python as both its scripting language and its source language.
Until a while ago, there was also support for a custom parsed language called "tzylang", but it's since been removed due to parsing related issues. 
Other scripting languages will probably be added in the futures (C# Being my main focus), but for now this is what you get

# Requirements
Capsian now incldues a Python Virtual Enviroment (venv) to insure everybody has the same experience, regardless of what they have installed on their machine.
This doesn't mean, though, that there's nothing you need or may want to do to improve your coding experience
- Windows 10 or macOS Catalina (Linux not supported for now)
- Microsoft Visual Studio Code with alle necessary extensions and the python interpreter set to "Python 3.7.3 venv"

Unfortunatelly I don't have a Linux machine (And not even a VM right now) which prevents me from creating a Linux venv, thus worsening your coding experience on Linux.
This doesn't mean you can't use Capsian on Linux though. Yuo can, it's just that you'll have to install pyglet 1.5.6 and Python 3.7.3 on your machine 

Visual Studio Code is a great editor as it doesn't force you to use your machine's Python Interpreter, but allows you to choose it. Read the next block for more information

# Setting up VS Code for Capsian
In the bottom-left of the VS Code window, you should see a few buttons
1. Clcik on "Python ..."
2. Click on "Enter Interpreter Path"
3. Click on "Find"
4. Navigate to the Project's folder
5. Go to "venv"
6. Open the folder with your OS name (Windows or macOS)
7. Double-click on "Scripts"
8. Select python (Not pythonw)

# Older versions
Did you know Capsian hasn't always been the name of this project? It was initially called KeyFire; the name was later changed due to trademark related issues and it became Capsian. You can still access all old versions, posts, issues etc on my private website which you can find a link for in my profile info.

# Myself
I am ALessandro Salerno, AKA tzyvoski. I was born in Italy and I still live there. And yes, I love Pizza 😂
I study IT in high school and have been working on Capsian (And its predecessors) for one and a half years. 

# Commits and branching
Please do NOT commit and push to the master branch, you can clone the repository or create another branch as stated by the license in the LICENSE.txt file
If you think your contributions could help a lot, then write to my email address (miro.salerno@icloud.com). I amy or may not accept the contribution and implement it in the engine directly. IN this case, you'll be listed in the credits

# Credits
All though I am the solo developer of Capsian, some people helped me and still help me, here are some of them
- Carpal (From the Italian Discord Server "RobinScript Community")
- Liam (From the Italian Discord Server "Tecnologia per Tutti")
- Lorenzo Bergadano (From Real life 
- Pyglet and the pyglet contributors for providing the amazing toolkit used to make Capsian

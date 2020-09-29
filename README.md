# Overview
Capsian is a weird, incomplete and performant Python game engine.
It was initially called "KeyFire Engine" but it was later renaemd to apsian due to trademark related issues.

# Performance
Capsian's performance are pretty great. All though written in Python, the engine's performance ae good at worst and amazing at best.
While testing, the highest framerate recorded was 169000 FPS, to make clear just how much this is, if you rendered exactly 60 frames per second, it would take you 46 minutes to ssee a simular amount of frames.
There are ares of the engine, such as 2D, that could be improved both in feature and in performance, but overall you are not gonna have big performance problems. 

ALL TESTS WERE CONDUCTED ON A GTX 1080 AND INTEL CORE i7 8700K 3.70GHz

# Languages
Capsian uses Python as both its scripting language and its source language.
Until a while ago, there was also support for a custom parsed language called "tzylang", but it's since been removed due to parsing related issues. 
Other scripting languages will probably be added in the futures (C# Being my main focus), but for now this is what you get

# Requirements
Capsian doesn't have any specific requirements, in its binary form, in fact, you actualy don't need anything. You don't even need python installed on your machine.
But there are a few things that may make your coding experience better
- Python 3.7 or 3.8 (Raccomended: 3.7)
- pyglet 1.5.6 or 1.5.7 (Raccomended: 1.5.7)
- "from locals import *" at the start of all your scripts
- Microsoft Visual Studio Code with all necessary python extensions

Having python installed will allow you to run Capsian even on pre-releases (Since they are not compiled in binary form) and will enable intellisense;
Having pyglet installed may fix a few crashes that you may experience due to "no module named ..." exceptions;
Importing everything from locals.py will allow python to recognize parts of your code and help you along the way;
VS Code is the IDE with which Capsian is built, with such large libraries a lite-weight editor is needed to insure stability while coding. 

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
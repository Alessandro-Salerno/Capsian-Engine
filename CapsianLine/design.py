from locals import *
from CapsianLine.commands import system

# Init the program
system.clear()


def draw():
    print("============================================================================")
    TermColor.begin(TermColor.OK_BLUE)
    print(f"CapsianLine v1.0 for {engine.version()}")
    print("Capsian: https://github.com/tzyvoski/Capsian-Engine")
    print("CapsianLine: https://github.com/Carpall/capsianline", end="\n")
    TermColor.end()

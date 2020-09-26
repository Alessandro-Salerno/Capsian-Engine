from pyglet.gl import *


fog_objs = []


class Fog:
    def __init__(self, color, start, end):
        for obj in fog_objs:
            del obj

        fog_objs.clear()
        self.enable()
        glFogfv(GL_FOG_COLOR, (GLfloat * 4)(color[0], color[1], color[2], color[3]))
        glHint(GL_FOG_HINT, GL_NICEST)
        glFogf(GL_FOG_MODE, GL_LINEAR)
        glFogf(GL_FOG_START, float(start))
        glFogf(GL_FOG_END, float(end))
        fog_objs.append(self)


    @staticmethod
    def enable():
        glEnable(GL_FOG)


    @staticmethod
    def disable():
        glDisable(GL_FOG)

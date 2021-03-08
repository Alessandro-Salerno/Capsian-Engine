from   Capsian import *
import random


class FlashingLight(AmbientLight):
    def flash(self, *args, **kwargs):
        offset = random.uniform(-30, 20)
        
        if not self.intensity[0] > 0:
            self.intensity[0] = 50
            self.intensity[1] = 50
            return

        if self.intensity[0] + offset > 5:
            self.intensity[0] += offset
            self.intensity[1] += offset

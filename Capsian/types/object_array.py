from locals import Log


class LimitedLenghtObjectArray(list):
    def __init__(self, max_size=128, auto_clear=False):
        self.max_size   = int(max_size)
        self.auto_clear = bool(auto_clear)


    def append(self, object):
        if len(self) < self.max_size:
            list.append(self, object)
        else:
            if self.auto_clear:
                self.clear()
            else:
                Log.error(f"Cannot add more than {self.max_size} objects to LimitedLenghtObjectArray")

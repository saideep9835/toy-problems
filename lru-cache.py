from collections import OrderedDict
class LRUcache:
    def __init__(self, capacity : int):
        self.cache = OrderedDict()
        self.capacity = capacity
from collections import OrderedDict
class LRUcache:
    def __init__(self, capacity : int):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
c = LRUcache(2)
c.put(1, 1)
print(c.cache)
c.put(2, 2)
print(c.cache)
c.get(1)
print(c.cache)
c.put(3, 3)
print(c.cache)
c.get(2)
print(c.cache)
c.put(4, 4)
print(c.cache)
c.get(1)
print(c.cache)
c.get(3)
print(c.cache)
c.get(4)
print(c.cache)
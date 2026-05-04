# RU Cache
# cache = LRUCache(2)

# cache.put(1,1)
# cache.put(2,2)
# cache.get(1)   # 1
# cache.put(3,3) # evicts 2
# cache.get(2)   # -1
# cache.put(4,4) # evicts 1
# cache.get(1)   # -1
# cache.get(3)   # 3
# cache.get(4)   # 4
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
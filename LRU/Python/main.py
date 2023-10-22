# Cache Replacement Policy in Python
from collections import OrderedDict

class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # move accessed item to the end
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            self.cache[key] = value
            self.cache.move_to_end(key)
        else:

            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

def main():
    cache = LRU(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

if __name__ == "__main__":
    main()
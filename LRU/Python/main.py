# Cache Replacement Policy in Python
# 'collections module implements specialized container datatypes providing alternatives to Python's general purpose'
from collections import OrderdDict

class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache - OrderDi
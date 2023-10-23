# Basic Funtionality 
import main

def test_basic_functionality():    
    cache = LRU(2)
    cache.put(1, 1)
    cache.put(2,2)
    assert cache.get(1) == 1 
    cache.put(3,3)
    assert cache.get(2) == -1
    cache.put(4,4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4 

# Overwriting an existing ket:

def test_overwrite_key():
    cache = LRU(2)
    cache.put(1,1)
    cache.put(2,2)
    cache.put(1,10)
    assert cache.get(1) == 10
    assert cache.get(1) == 2


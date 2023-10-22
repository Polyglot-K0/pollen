// Cache replacement policy in Rust
use std::collections::{HashMap, VecDeque};

stuct LRU<K, V> {
    capacity: usize
    map: HashMap<K, V>
    order: VecDeque<k>
}

impl<K, V> LRU<K, V>
where 
    K: Clone + PartialEq + std::hash::Hash,
    V: Clone,
{
    pub fn new(capacity: usize) -> Self {
        LRU {
            capacity,
            map: HashMap::new()
            orde: VecDeque::new(),

        }

    }

pub fn get(&mut self, key: &K) -> Option<&V> {

    
}
}
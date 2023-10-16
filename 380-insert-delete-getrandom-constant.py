#Solution 1 (O(n) get random)
import random
class RandomizedSet:

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        self.data.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.data))
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


import random
class RandomizedSet:

    def __init__(self):
        self.data = []
        self.added = {}

    def insert(self, val: int) -> bool:
        if val in self.added:
            return False
        self.data.append(val)
        self.added[val] = len(self.data) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.added:
            return False
        old_last = len(self.data) - 1
        swap_index = self.added[val]
        last_val = self.data[-1]
        self.data[swap_index], self.data[-1] = self.data[-1], self.data[swap_index]
        self.data.pop()

        #Remove from hashmap
        del self.added[val]
        if old_last != swap_index:
            self.added[last_val] = swap_index
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
        
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.remove(0)
param_2 = obj.remove(0)
param_3 = obj.insert(0)
param_4 = obj.getRandom()
param_5 = obj.remove(0)
param_6 = obj.insert(0)
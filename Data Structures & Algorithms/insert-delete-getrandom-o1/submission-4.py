class RandomizedSet:

    def __init__(self):
        self.data = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.data.append(val)
        self.index[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        i = self.index[val]
        j = len(self.data)-1
        swap = self.data[j]
        self.data[i], self.data[j] = swap, val
        self.index[swap] = i
        self.data.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
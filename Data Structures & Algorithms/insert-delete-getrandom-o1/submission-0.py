class RandomizedSet:

    def __init__(self):
        self.values = [] # stores values and allows for O(1) removal
        self.map = {} # stores values to index in array

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.values.append(val)
            self.map[val] = len(self.values) - 1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            # swap value with value at the end
            tmp = self.values[-1]
            self.values[-1] = self.values[self.map[val]]
            self.values[self.map[val]] = tmp
            self.map[tmp] = self.map[val]
            del self.map[val]
            self.values.pop()
            return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
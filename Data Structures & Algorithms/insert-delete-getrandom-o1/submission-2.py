import random
class RandomizedSet:
    def __init__(self):
        self.values = []
        self.hashmap = {} # stores value : index

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.values.append(val)
            self.hashmap[val] = len(self.values) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        else:
            idx = self.hashmap[val]
            last_val = self.values[-1]

            # most last elt into the remov(ing) items spot
            self.values[idx] = last_val
            self.hashmap[last_val] = idx

            self.values.pop()
            del self.hashmap[val]
            return True

        

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
import random
class RandomizedSet:
    '''
    keep values in a list, and a dict {val:idx}
    insert: check membership in dict, add and append to values list
    remove: check membership in dict, swap val and lastVal, then remove
    getRandom: get random from values arr
    '''
    def __init__(self):
        self.values = []
        self.idxs = {}

    def insert(self, val: int) -> bool:
        if val not in self.idxs:
            self.idxs[val] = len(self.values)
            self.values.append(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:   
        if val in self.idxs:
            valIdx = self.idxs[val]
            lastVal = self.values[-1]

            # swap last value and value to remove idx, remove anyways
            self.values[valIdx] = lastVal
            self.values.pop()

            # remove val from dict and update swapped val idx
            self.idxs[lastVal] = valIdx
            self.idxs.pop(val)

            return True
        return False
            
    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
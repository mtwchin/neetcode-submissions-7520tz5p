class TimeMap:
    '''
    note: solution below more efficient time-complexity-wise
    b/c using default dict we dont waste time comparing membership ofself.keyvalues
    '''
    from collections import defaultdict

    def __init__(self):
        self.keyvalues = defaultdict(list) # store as list and append because inc.

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyvalues[key].append((timestamp, value))
    
    '''
    curently, nested hashmap stores the data values as 
    keyvalues[key] = [[t1, v1], [t2, v2], [t3, v3], ... [tn, vn]]
    '''



    '''
    if the key does not exist, return ""
    perform binary search on the keystore[key] array to find the rightmost timestamp
        - do this by checking "if values[mid][0] <= timestamp"": return values[mid][1], and l = mid + 1
        - if found, return the correct value and if not return "" as default res value set earlier
    '''
    def get(self, key: str, timestamp: int) -> str:
        # if called with no valid timestamp value, return latest possible timestamp value
        if key not in self.keyvalues:
            return ""

        values = self.keyvalues[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
            



        return res
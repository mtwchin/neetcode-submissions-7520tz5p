class TimeMap:
    '''
    nested hashmap?
    hashmap 1: {key:timestamps}
    timestamps:[value:time]
    timestamp sets are in strictly increasing order. can use binary search to find 
        value @ specific time 
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
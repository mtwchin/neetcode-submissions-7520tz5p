class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # hashmap, counts each char and returns hashmap for it
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # we want most freq, except prev
            cnt, char = heapq.heappop(maxHeap) #returns pair of values cnt, char
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        return res
            
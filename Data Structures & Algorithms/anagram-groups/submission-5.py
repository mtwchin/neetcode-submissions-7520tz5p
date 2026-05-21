class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freqArr = [0] * 26
            for char in s:
                freqArr[ord(char) - ord('a')] += 1
            res[tuple(freqArr)].append(s)
        return list(res.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            # for each str, hold a freq arr
            for char in s:
                freq[ord(char) - ord('a')] += 1
            # after this, you should have a full freq arr for cur str
            anagrams[tuple(freq)].append(s)
        return list(anagrams.values())
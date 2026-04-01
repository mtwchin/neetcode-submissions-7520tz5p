class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping frequency array to to list of anagrams
        out = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a-z, one space for each char
            for c in s:
                # map a to 0, b to 1, etc
                # if ord("a") = 80, 80-80=0, if ord("b")=81, 81-80=1 so b->1
                count[ord(c)-ord("a")] += 1
            out[tuple(count)].append(s)
        return list(out.values())


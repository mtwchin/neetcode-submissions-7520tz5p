class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping frequency array to to list of anagrams

        out = defaultdict(list) #to ensure list to append to in line 13

        for s in strs:
            count = [0] * 26 # a-z, one space for each char
            for c in s:
                # if ord("a") = 80, 80-80=0, if ord("b")=81, 81-80=1 so b->1
                # map a to 0, b to 1, etc
                count[ord(c)-ord("a")] += 1 # go to the cth index in the frequency array and increment it 
            out[tuple(count)].append(s) # tuple because hashmap keys must be immutable and unique
        return list(out.values())


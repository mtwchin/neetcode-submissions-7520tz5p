class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        the idea is to create a frequency array of the chars that come up in the str
        and make a hashmap mapping the freq arr to the strings that match
        then print the hm.values() at the end
        '''
        hm = {}

        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]
        return list(hm.values())
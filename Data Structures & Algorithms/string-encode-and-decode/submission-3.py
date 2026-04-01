class Solution:
    '''
    encode list of strings into a string
        for each string, append # and add the next
        return the res
    decode string back into list of strings
    '''
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0

        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[index:j])
            index = j + 1
            j = index + length
            res.append(s[index:j])
            index = j
        return res

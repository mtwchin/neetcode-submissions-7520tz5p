class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out+=str(len(i)) + "#" + i
        return out

    def decode(self, s: str) -> List[str]:
        out,i = [],0
        while i < len(s):
            j=i
            # Getting length of the word (grab number prefix)
            while s[j] != "#":
                j+=1
            wordlen = int(s[i:j])            
            # Move i to front of word
            i=j+1
            # Move j to end of word using i+wordlen
            j=i+wordlen
            # Append sliced word
            out.append(s[i:j])
            # Move i up to j (end of word)
            i=j

        return out


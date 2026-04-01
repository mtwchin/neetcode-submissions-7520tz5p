class Solution:
    def decodeString(self, s: str) -> str:
        sta = []

        for i in range(len(s)):
            if s[i] != "]":
                sta.append(s[i])
            else:
                temp = ""
                while sta[-1] != "[":
                    temp = sta.pop() + temp
                sta.pop()
                k = ""
                while sta and sta[-1].isdigit():
                    k = sta.pop() + k
                sta.append(int(k) * temp)
        return "".join(sta)

            

            
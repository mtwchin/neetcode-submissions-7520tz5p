class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for r in range(len(digits)-1, -1, -1):
            if digits[r] < 9:
                digits[r] += 1
                return digits
            digits[r] = 0
        # meaning you hit all 9s
        return [1] + digits

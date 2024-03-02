class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count = -1
        for char in s:
            if char == '1':
                count += 1
        
        res = '1'*count + '0'*(n-count-1) + '1'

        return res
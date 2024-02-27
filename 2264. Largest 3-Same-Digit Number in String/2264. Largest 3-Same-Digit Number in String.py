class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_val = "-1"
        i = 0
        while i < len(num)-2:
            if num[i] == num[i+1] == num[i+2]:
                max_val = max(max_val, num[i])
                i += 3
            else:
                i += 1
        
        return max_val * 3 if max_val != "-1" else ""
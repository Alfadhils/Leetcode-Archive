class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x<0 else 1
        res = int(str(abs(x))[::-1])*neg
        false = -(2**31) <= res <= 2**31 - 1
        return res if false else 0
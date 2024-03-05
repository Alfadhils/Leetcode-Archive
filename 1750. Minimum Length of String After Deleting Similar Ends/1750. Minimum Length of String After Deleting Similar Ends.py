class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        left, right = 0, n-1
        while left < right:
            curr = s[left]
            if s[right] != curr:
                break

            while s[left] == curr and left < n-1:
                left += 1
            while s[right] == curr and right > 0:
                right -= 1

        if right>=left:
            return right-left+1
        else :
            return 0
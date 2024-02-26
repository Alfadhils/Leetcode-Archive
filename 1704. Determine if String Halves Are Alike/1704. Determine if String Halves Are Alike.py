class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        left = s[:n//2].lower()
        right = s[n//2:].lower()
        vowel = ['a','i','u','e','o']
        left_count = 0
        right_count = 0
        for i in vowel:
            if i in left:
                left_count += left.count(i)
                
            if i in right:
                right_count += right.count(i)

        return left_count == right_count
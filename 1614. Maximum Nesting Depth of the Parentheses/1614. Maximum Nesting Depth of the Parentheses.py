class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxdepth = 0
        for char in s:
            if char == '(':
                depth += 1
                maxdepth = max(maxdepth, depth)
            elif char == ')':
                depth -= 1
 
        return maxdepth
        
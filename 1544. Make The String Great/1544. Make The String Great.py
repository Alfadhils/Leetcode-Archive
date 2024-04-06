class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if stack :
                prev = stack[-1]
                if s[i] != prev and (s[i] == prev.upper() or s[i] == prev.lower()):
                    stack.pop()
                    continue
            
            stack.append(s[i])

        return ''.join(stack)
        
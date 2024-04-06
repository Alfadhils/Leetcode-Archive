class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        excess = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    excess.add(i)
        
        excess.update(stack) 
        
        return ''.join(char for i, char in enumerate(s) if i not in excess)
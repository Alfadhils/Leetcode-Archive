# Intuition
The intuition behind this approach is to iterate through each character in the ransom note and check if it exists in the magazine. If it does, remove that character from the magazine; otherwise, return False. If we successfully iterate through all characters in the ransom note, return True.

# Approach
1. Iterate through each character in the ransom note.
2. Check if the character exists in the magazine.
3. If it does, remove that character from the magazine using `replace`.
4. If the character doesn't exist in the magazine, return False.
5. If we successfully iterate through all characters in the ransom note, return `True`.

# Complexity
- Time complexity: `O(m * n)`, where `m` is the length of the ransom note and `n` is the length of the magazine. In the worst case, for each character in the ransom note, we might have to perform a linear search in the magazine.
- Space complexity: `O(1)`, as we are not using any additional space that grows with the input.

# Code
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, '', 1)
            else:
                return False
        return True

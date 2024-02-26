# 387. First Unique Character in a String

## Intuition
To solve this problem, we can iterate through the string to count the occurrences of each character using a Counter. Then, we iterate through the string again and return the index of the first character with a count of 1.

## Approach
1. Use a Counter to count the occurrences of each character in the string.
2. Iterate through the string and return the index of the first character with a count of 1.

## Complexity
- Time complexity: O(n), where n is the length of the string. We iterate through the string twice, once to build the Counter and once to find the first unique character.
- Space complexity: O(n), where n is the length of the string. We use extra space to store the Counter.

## Code
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] < 2:
                return i 
                
        return -1
```
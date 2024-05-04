# 1915. Number of Wonderful Substrings
## Intuition
The problem seems like it involves counting substrings of a given string that are wonderful. A substring is wonderful if it contains at most one odd count character. This suggests that we might need to keep track of character counts within substrings.

## Approach
One way to approach this problem is by using bit manipulation. We can represent the counts of characters using a bitmask, where each bit represents whether the count of a character is odd or even. If a bit is set to 1, it indicates an odd count, and if it's set to 0, it indicates an even count.

We iterate through the string, updating the bitmask for each character encountered. For each position, we check how many wonderful substrings can be formed ending at that position. To do this, we consider all possible substrings ending at the current position and check if they are wonderful. We can achieve this by considering all possible bitmasks that can be obtained by toggling a single bit in the current bitmask.

We keep track of the count of each bitmask encountered using a dictionary, `bitmask_count`. This dictionary stores the count of each bitmask encountered so far.

## Complexity
- Time complexity:
    - The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the string once.
- Space complexity:
    - The space complexity is also O(n) because we use a dictionary to store the count of each bitmask encountered.

## Code
```python
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitmask_count = {0: 1}
        bitmask = 0
        res = 0
        
        for char in word:
            bitmask ^= 1 << (ord(char) - ord('a'))
            
            res += bitmask_count.get(bitmask, 0)
            for i in range(10):
                alt_bitmask = bitmask ^ (1 << i)
                res += bitmask_count.get(alt_bitmask, 0)
            
            bitmask_count[bitmask] = bitmask_count.get(bitmask, 0) + 1

        return res
```

# 1662. Check If Two String Arrays are Equivalent

## Intuition
To solve this problem, we can concatenate all strings in each array and then compare the resulting strings to check if they are equivalent.

## Approach
The approach is to concatenate all strings in `word1` and `word2` arrays using the join() function, and then compare the resulting strings. If the concatenated strings are equal, return `True`, otherwise return `False`.

## Complexity
- Time complexity:
Concatenating all strings in each array takes linear time proportional to the total length of all strings in the arrays. Therefore, the time complexity is O(n), where n is the total number of characters in both arrays.

- Space complexity:
We are creating two new strings by concatenating all strings in the arrays. Therefore, the space complexity is O(n), where n is the total number of characters in both arrays.

## Code
``` python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
        
```

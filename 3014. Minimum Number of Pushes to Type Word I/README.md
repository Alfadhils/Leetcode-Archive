# 3014. Minimum Number of Pushes to Type Word I
## Intuition
To solve this problem, we need to find the minimum number of pushes needed to type the given word after remapping the keys. Since each letter on the keypad requires a certain number of pushes, we can iterate through each letter in the word and calculate the number of pushes required based on the position of the letter on the keypad.

## Approach
- Iterate through each letter in the word.
- Calculate the number of pushes required for each letter based on its position on the keypad.
- Sum up the total number of pushes required for all letters.
- Return the total number of pushes.

## Complexity
- Time complexity: O(n), where n is the length of the word.
- Space complexity: O(1), as we are using constant space.

## Code
```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        for i in range(len(word)):
            inc = i//8 + 1
            res += inc
            
        return res
```
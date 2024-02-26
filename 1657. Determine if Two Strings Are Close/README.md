# 1657. Determine if Two Strings Are Close

## Intuition
The intuition behind this problem is to recognize that two strings can be considered **close** if they have the same set of characters with the same frequencies, regardless of the order of characters. Therefore, we need to devise a way to check whether the two strings satisfy this condition.

## Approach
The approach is to check if the two strings can be transformed into each other by performing only two types of operations:
1. Rearranging characters.
2. Swapping any two characters.

## Complexity
- Time complexity: 
    - Counting the occurrences of characters in both strings takes O(n) time, where n is the length of the longer string.
    - Sorting the lists of character counts takes O(m log m) time, where m is the number of unique characters in the strings.
    - Overall, the time complexity is O(n + m log m).

- Space complexity:
    - Storing the Counters requires O(m) space, where m is the number of unique characters in the strings.
    - Sorting the lists of character counts also requires O(m) space.
    - Overall, the space complexity is O(m).

## Code
``` python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
            
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)

        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
        
```
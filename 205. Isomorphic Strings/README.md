# 205. Isomorphic Strings

## Intuition
Isomorphic strings are strings where characters in one string can be mapped to characters in another string such that all occurrences of each character in the first string map to the same character in the second string. 

## Approach
One way to check if two strings are isomorphic is to compare the set of characters in both strings and the set of pairs of corresponding characters. If the lengths of these sets are equal, it means that each character in one string is mapped to exactly one character in the other string, maintaining the isomorphic property. 

## Complexity
- Time complexity: O(n), where n is the length of the input strings. 
  - The `set()` function takes O(n) time to construct the set of characters for both strings.
  - The `zip()` function takes O(n) time to generate pairs of characters.
- Space complexity: O(n), where n is the length of the input strings.
  - Additional space is used to store the sets of characters and pairs of characters.

## Code
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))

```
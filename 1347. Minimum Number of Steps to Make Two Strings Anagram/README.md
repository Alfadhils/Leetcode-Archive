# 1347. Minimum Number of Steps to Make Two Strings Anagram

## Intuition
The problem involves finding the minimum number of steps required to make two strings anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase.

## Approach
The approach involves counting the frequency of characters in both strings using Counter from the collections module. Then, iterate through the frequencies of characters in one string and find the difference between the frequencies in both strings. If the difference is positive, it means there are excess characters in the first string, which need to be replaced. Add up all such differences to get the total number of steps required.

## Complexity
- Time complexity: O(n), where n is the length of the input string `s` or `t`. Counting the frequency of characters and iterating through them takes linear time.
- Space complexity: O(n), where n is the number of unique characters in the input string `s`. The space complexity is dominated by the Counter dictionary created to store the frequencies of characters.

## Code
```python
import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = collections.Counter(s)

        total = 0
        for char in freq.keys():
            diff = freq[char] - t.count(char)
            if diff > 0:
                total += diff
        return total
```

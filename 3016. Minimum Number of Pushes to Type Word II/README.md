# 3016. Minimum Number of Pushes to Type Word II

## Intuition
The problem requires finding the minimum number of times the keys need to be pushed to type a given word. Since each key on a telephone keypad maps to a distinct collection of lowercase English letters, we can exploit the frequency of letters in the word to minimize the number of pushes. By assigning the most frequently occurring letters to keys that require fewer pushes, we can optimize the typing process.

## Approach
1. Count the frequency of each letter in the word.
2. Sort the letters based on their frequencies in descending order.
3. Assign keys to letters starting from the most frequent ones.
4. Calculate the minimum number of pushes required for each key based on its frequency.
5. Accumulate the total number of pushes required.

## Complexity
- Time complexity:
    - Counting the frequency of letters: O(n), where n is the length of the word.
    - Sorting the letters: O(m log m), where m is the number of distinct letters in the word (at most 26).
    - Calculating pushes: O(m)
    Overall time complexity is O(n + m log m).
- Space complexity:
    - Counting the frequency of letters: O(m)
    - Sorting: O(m)
    Overall space complexity is O(m).

## Code
```python
import collections

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_counter = collections.Counter(word)
        
        sorted_letters = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)
        
        total_pushes = 0
        
        for i, (letter, frequency) in enumerate(sorted_letters):
            pushes = (i // 8) + 1
            total_pushes += pushes * frequency
        
        return total_pushes

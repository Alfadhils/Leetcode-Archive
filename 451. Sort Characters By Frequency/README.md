# 451. Sort Characters By Frequency

## Intuition
The problem asks to sort characters in a string based on their frequency. An intuitive approach is to count the frequency of each character and then sort them based on their frequency.

## Approach
We can use a dictionary or a Counter to count the frequency of each character in the string. Then, we can sort the characters based on their frequency and concatenate them accordingly.

## Complexity
- Time complexity:
  - Counting the frequency of characters takes O(n), where n is the length of the string.
  - Sorting the characters based on frequency takes O(k log k), where k is the number of unique characters.
  - Concatenating the characters takes O(k), where k is the total number of characters in the string.
  - Therefore, the overall time complexity is O(n + k log k).

- Space complexity:
  - We use a Counter object to store the frequency of characters, which takes O(k) space, where k is the number of unique characters.
  - The space required for the output string is also O(k).
  - Therefore, the overall space complexity is O(k).

## Code
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        for char, freq in c.most_common():
            ans += char * freq
        
        return ans
```
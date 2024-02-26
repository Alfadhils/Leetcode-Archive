# 1704. Determine if String Halves Are Alike

## Intuition
The intuition behind this problem is to divide the given string into two halves and then count the number of vowels in each half. If the count of vowels in both halves is equal, then the two halves are considered **alike**.

## Approach
The approach is to divide the string into two halves and count the number of vowels in each half. We convert both halves to lowercase to simplify the comparison. Then, we iterate through each vowel and count its occurrences in both halves. Finally, we check if the counts of vowels in both halves are equal.

## Complexity
- Time complexity: (O(n)) where (n) is the length of the input string `s`. This is because we iterate through the string once to count the vowels.
  
- Space complexity: (O(1)) since we use a fixed-size array to store the vowels and a constant amount of additional space for variables and counting.

## Code
```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        left = s[:n//2].lower()
        right = s[n//2:].lower()
        vowel = ['a', 'i', 'u', 'e', 'o']
        left_count = 0
        right_count = 0
        for i in vowel:
            if i in left:
                left_count += left.count(i)
                
            if i in right:
                right_count += right.count(i)

        return left_count == right_count
```
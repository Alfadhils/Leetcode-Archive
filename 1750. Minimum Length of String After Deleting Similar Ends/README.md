# 1750. Minimum Length of String After Deleting Similar Ends

## Intuition
The problem asks us to find the length of a string after removing characters from both ends under the condition that both characters at the ends are the same. We can solve this using a two-pointer approach to traverse the string from the left and right simultaneously.

## Approach
Using two pointers, we define `left` and `right` as index pointers for the string. We use a while loop as long as `left` is less than `right`. We take the character from the `left` pointer and use it as our current character `curr`. While the characters at both `left` and `right` are the same as `curr`, we move both the `left` and `right` pointers towards the center until the condition breaks. Then, we take the difference between `left` and `right`.

## Complexity
- Time complexity: O(n), where n is the length of the string. The two pointers traverse each element once.
- Space complexity: O(1), as we use a constant amount of space.

## Code
```python
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        left, right = 0, n-1
        while left < right:
            curr = s[left]
            if s[right] != curr:
                break

            while s[left] == curr and left < n-1:
                left += 1
            while s[right] == curr and right > 0:
                right -= 1

        if right >= left:
            return right - left + 1
        else:
            return 0
```
# 9. Palindrome Number

## Intuition

The problem involves determining whether an integer is a palindrome. My initial intuition is to convert the integer to a string and check if the string is equal to its reverse.

## Approach

The approach is to convert the integer to a string and compare it with its reverse. If the string representation is the same when reversed, the integer is a palindrome.

## Complexity

- Time complexity:

The time complexity of this solution is O(log(n)), where n is the value of the input integer. This is because we are converting the integer to a string, which takes O(log(n)) time.

- Space complexity:

The space complexity is O(log(n)) as we need space to store the string representation of the integer.

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
```

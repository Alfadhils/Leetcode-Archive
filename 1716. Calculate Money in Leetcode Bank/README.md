# 1716. Calculate Money in Leetcode Bank

## Intuition
The problem requires calculating the total amount of money you will have in your Leetcode bank after performing certain transactions. 

## Approach
To solve this problem, we can simulate the process of depositing money into the bank. We iterate through each day, keeping track of the total money based on the current day of the week and the number of weeks that have passed. We add the money deposited on each day to the total amount. 

## Complexity
- Time complexity: O(n), where n is the number of days for which we need to calculate the total money.
- Space complexity: O(1), as we are not using any extra space that grows with the input size.

## Code
```python
class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(n):
            res += (i % 7 + 1) + i // 7
        return res
```

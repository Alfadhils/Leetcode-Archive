# 1672. Richest Customer Wealth
## Intuition
The problem seems to be asking to find the richest customer in terms of wealth. We need to iterate through each customer's accounts, calculate their wealth, and keep track of the maximum wealth found so far.

## Approach
1. Initialize a variable `maxwealth` to store the maximum wealth found so far. Set it to the sum of the first customer's accounts.
2. Iterate through each customer's accounts.
3. For each customer, calculate their wealth by summing up all their account balances.
4. If the calculated wealth is greater than `maxwealth`, update `maxwealth` to the new calculated wealth.
5. After iterating through all customers, return `maxwealth`.

## Complexity
- Time complexity:
    - The algorithm iterates through each customer's accounts once, performing constant time operations within each iteration. So, the time complexity is O(n), where n is the number of customers.
- Space complexity:
    - The algorithm uses only a constant amount of extra space for variables regardless of the input size. Thus, the space complexity is O(1).

## Code
``` python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = sum(accounts[0])
        for i in accounts:
            if sum(i)> maxwealth:
                maxwealth = sum(i)
        return maxwealth
        
```
# 2147. Number of Ways to Divide a Long Corridor

## Intuition
The problem seems to involve counting the number of ways to divide a long corridor based on certain conditions.

## Approach
1. Iterate through the corridor string.
2. Keep track of the number of `S` characters encountered.
3. Whenever an `S` is encountered, check if the count is odd or even.
4. If odd, append the current count of ways to the result list and reset the count of ways.
5. If `P` is encountered and the count of `S` is even, increment the count of ways.
6. After iterating through the corridor, if the count of `S` is odd or less than 2, return 0.
7. Otherwise, calculate the total number of ways using the counts stored in the result list.
8. Return the total modulo (10^9 + 7).

## Complexity
- Time complexity: O(n), where n is the length of the corridor string.
- Space complexity: O(n), where n is the number of `S` characters encountered in the corridor.

## Code
```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        scount, ways, total, res = 0, 0, 1, []

        for char in corridor:
            if char == 'S':
                if scount % 2:
                    res.append(ways)
                    ways = 0
                scount += 1
            elif char == 'P' and not scount % 2:
                ways += 1

        if scount % 2 or scount < 2:
            return 0

        for num in res[1:]:
            total = (total * (num + 1)) % (10**9 + 7)

        return total
```
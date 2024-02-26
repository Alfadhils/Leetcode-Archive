# 1688. Count of Matches in Tournament

## Intuition
The problem likely involves counting the total number of matches played in a tournament, given the number of teams participating. Typically, in a tournament where each match results in one team being eliminated until only one team remains, the number of matches can be determined based on the number of teams.

## Approach
The approach here is to keep track of the number of matches played at each stage of the tournament. At each stage, half of the teams get eliminated, except in the final stage where only one team remains. This process continues recursively until there's only one team left.

## Complexity
- Time complexity: O(log n)
  - Each recursive call reduces the number of teams by half, resulting in a logarithmic time complexity.
- Space complexity: O(log n)
  - The space complexity is determined by the recursive calls on the call stack, which is also logarithmic.

## Code
```python
class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n < 2:
            return 0

        matches = n // 2
        return matches + self.numberOfMatches(n - matches)
```
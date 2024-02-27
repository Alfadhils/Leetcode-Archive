# 2225. Find Players With Zero or One Losses

## Intuition
The problem likely involves parsing through a list of matches to identify players with zero or one losses. It's a straightforward task of counting the number of losses for each player and categorizing them accordingly.

## Approach
1. Initialize a dictionary `win` to keep track of the number of losses for each player.
2. Iterate through the list of matches. For each match:
   - If the player doesn't exist in the `win` dictionary, add them with zero losses.
   - If the opponent exists in the `win` dictionary, increment their loss count. If not, add them with one loss.
3. After processing all matches, iterate through the `win` dictionary:
   - If a player has zero losses, add them to the `res1` list.
   - If a player has one loss, add them to the `res2` list.
4. Return the sorted lists `res1` and `res2` as the result.

## Complexity
- Time complexity: \(O(n)\), where \(n\) is the number of matches. We iterate through the list of matches once to count losses.
- Space complexity: \(O(n)\), where \(n\) is the number of players. The space required is primarily for storing the `win` dictionary and the result lists.

## Code
```python
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        res1 = []
        res2 = []
        for match in matches:
            if match[0] not in win:
                win[match[0]] = 0

            if match[1] in win:
                win[match[1]] += 1
            else:
                win[match[1]] = 1
        
        for key in win:
            if win[key] == 0:
                res1.append(key)
            elif win[key] == 1:
                res2.append(key)

        return [sorted(res1), sorted(res2)]
```

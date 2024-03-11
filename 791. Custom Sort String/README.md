# 791. Custom Sort String
## Intuition
The problem requires rearranging characters in string `s` based on the custom order provided in string `order`. We can achieve this by first creating a mapping of characters in `order` along with their respective positions, and then sorting the characters in `s` based on this mapping.

## Approach
1. Create a defaultdict to store the positions of characters in `order`.
2. Iterate through `order` and store the position of each character.
3. Define a custom function `getval` to retrieve the position of characters from the defaultdict.
4. Convert string `s` to a list and sort it based on the custom function `getval`.
5. Join the sorted list and return the result.

## Complexity
- Time complexity:
    - Constructing the defaultdict takes O(len(order)) time.
    - Sorting the characters in `s` takes O(len(s) * log(len(s))) time.
    - Overall time complexity is O(len(order) + len(s) * log(len(s))).

- Space complexity:
    - We use additional space to store the defaultdict and the list of characters in `s`.
    - Overall space complexity is O(len(order) + len(s)).

## Code
```python
from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        positions = defaultdict(int)
        for i, char in enumerate(order):
            positions[char] = i
        
        def getVal(c):
            return positions[c]
        
        s_list = list(s)
        s_list.sort(key=getVal)

        return ''.join(s_list)
```

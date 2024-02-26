# 2125. Number of Laser Beams in a Bank

## Intuition
To solve this problem, we need to find the total number of laser beams that can be formed by pairs of '1's in consecutive rows of the bank. This suggests iterating through each pair of consecutive rows, counting the number of '1's in each row, and multiplying these counts to get the number of laser beams formed by that pair.

## Approach
1. Iterate through each pair of consecutive rows in the bank.
2. Count the number of '1's in each row.
3. Multiply the counts of '1's in each row to get the number of laser beams formed by that pair.
4. Sum up the total number of laser beams formed by all pairs of consecutive rows.

## Complexity
- Time complexity: 
    - The time complexity of this approach is O(n), where n is the total number of elements in the bank.
- Space complexity:
    - The space complexity is O(1) because we're not using any extra space proportional to the size of the input.

## Code
```python
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) < 2:
            return 0

        total = 0
        i = 0
        while True:
            c = bank[i].count('1')
            while '1' not in bank[i+1]:
                if i + 1 == len(bank) - 1:
                    break
                i += 1

            n = bank[i+1].count('1')
            total += c * n
            
            if i + 1 == len(bank) - 1:
                break
            i += 1
        
        return total
```
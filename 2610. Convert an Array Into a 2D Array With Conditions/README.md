# 2610. Convert an Array Into a 2D Array With Conditions

## Intuition
To solve this problem, we need to create a 2D array from the given integer array `nums` while satisfying the following conditions:
1. The 2D array should contain only the elements of the array `nums`.
2. Each row in the 2D array should contain distinct integers.
3. The number of rows in the 2D array should be minimal.

## Approach
1. First, we sort the `nums` array.
2. We iterate through the sorted `nums` array and create rows for the 2D array.
3. We ensure that each row contains distinct integers.
4. Finally, we construct the output 2D array with minimal rows.

## Complexity
- Time complexity:  O(n log n) , where  n  is the length of the input `nums` array due to sorting.
- Space complexity:  O(n)  for storing the output 2D array.

## Code
```python
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        j = 0
        
        for i in range(len(nums)):
            if i < 1 or nums[i] == nums[i - 1]:
                res[j].append(nums[i])
            else:
                res.append([nums[i]])
                j += 1
        
        output_list = []
        
        max_length = max(len(sublist) for sublist in res)
        
        for i in range(max_length):
            new_sublist = []
            for sublist in res:
                if i < len(sublist):
                    new_sublist.append(sublist[i])
            output_list.append(new_sublist)
        
        return output_list
```

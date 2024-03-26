# 41. First Missing Positive

## Intuition
The intuition behind this problem is to find the smallest positive integer that does not exist in the given list of integers.

## Approach
The approach involves iterating through the list of integers and checking for positive integers starting from 1. We first remove duplicates from the list using set(). Then, we sort the list to ensure that positive integers are in ascending order. We initialize a variable `curr` to keep track of the current expected positive integer starting from 1. We iterate through the sorted list, and if we encounter a positive integer equal to `curr`, we increment `curr`. If we find a positive integer greater than `curr`, we know that `curr` is the first missing positive integer and we break out of the loop. Finally, we return `curr` which represents the first missing positive integer.

## Complexity
- Time complexity:  
   - Removing duplicates using set(): O(n)
   - Sorting the list: O(n log n)
   - Iterating through the sorted list: O(n)
   - Overall time complexity: O(n log n)
   
- Space complexity:
   - We use extra space to store the unique elements in the set: O(n)
   - Overall space complexity: O(n)

## Code
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums)) 
        nums.sort()  
        curr = 1  
        
        for n in nums:
            if n > 0:
                if n == curr:
                    curr += 1
                else:
                    break
        
        return curr
```
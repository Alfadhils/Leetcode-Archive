# 2870. Minimum Number of Operations to Make Array Empty

## Intuition
The problem requires counting the minimum number of operations needed to make the array empty by deleting either pairs or triplets of equal elements. The intuition here is to count the occurrences of each element in the array and then calculate the number of operations needed based on these counts.

## Approach
1. Create a dictionary `n_dict` to store the count of occurrences of each element in the array.
2. Iterate through the array and update the counts in `n_dict`.
3. Initialize a variable `count` to keep track of the total number of operations needed.
4. Iterate through the values in `n_dict` and calculate the number of operations needed for each count.
5. Return the total count of operations.

## Complexity
- Time complexity: O(n), where n is the length of the input array `nums`.
- Space complexity: O(n), where n is the number of unique elements in `nums`.

## Code
```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_dict = {}
        for n in nums:
            if n in n_dict:
                n_dict[n] += 1
            else:
                n_dict[n] = 1
        
        count = 0 
        for val in n_dict.values():
            if val == 1:
                return -1  
            count += (val - 1) // 3 + 1
        
        return count
```

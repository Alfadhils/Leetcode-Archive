# 169. Majority Element
## Intuition
One of the most efficient approaches to finding the majority element in an array is to use Boyer-Moore Voting Algorithm. This algorithm relies on the fact that if an element occurs more than n/2 times in an array (where n is the size of the array), then it will survive even after cancelling out all other elements. 

## Approach
1. Start with an assumption that the first element of the array is the majority element.
2. Iterate through the array, and for each element, if it matches the current assumed majority element, increase the count. If it's different, decrease the count.
3. If the count becomes zero, update the current element as the assumed majority element and reset the count.
4. The majority element will be the one that survives till the end.

## Complexity
- Time complexity: O(n) - We traverse the array once.
- Space complexity: O(1) - We are using constant space.

## Code
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        curr = nums[0]

        for n in nums[1:]:
            if curr == n:
                count += 1
            elif count == 0:
                curr = n
                count = 1
            else:
                count -= 1

        return curr
```

# 27. Remove Element

## Intuition
The intuition for solving this problem is to iterate through the list while maintaining two pointers, one for iterating through the list (`i`) and another for keeping track of the removed elements (`j`). Whenever we encounter the target value to be removed, we append it to the end of the list and pop it from its current position, effectively removing it. We increment the `j` counter to keep track of the number of removed elements.

## Approach
The approach involves using two pointers (`i` and `j`) to iterate through the list and remove the target element (`val`). Whenever we encounter the target element at index `i`, we append it to the end of the list and pop it from its current position. We increment the `j` counter to keep track of the number of removed elements.

## Complexity
- Time complexity:
  The time complexity of this approach is O(n), where n is the length of the input list `nums`. This is because we traverse the list once to remove the target element.
  
- Space complexity:
  The space complexity is O(1) because we are not using any extra space proportional to the size of the input list. We are only using constant space for storing the indices `i` and `j`.

## Code
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while i < len(nums)-j:
            if nums[i] == val:
                nums.append(nums.pop(i))
                j += 1
            else:
                i += 1
    
        return len(nums)-j
```
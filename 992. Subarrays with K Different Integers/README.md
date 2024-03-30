# 992. Subarrays with K Different Integers

## Intuition
The problem requires finding the number of subarrays with exactly K distinct integers. One intuitive approach could be to use a sliding window technique to find all possible subarrays and then count the number of distinct integers within those subarrays.

## Approach
1. Use two pointers `left1` and `left2` to represent the start of the window.
2. Use two dictionaries `count1` and `count2` to keep track of the count of each number in the current window for two different cases.
3. Use two variables `distinct1` and `distinct2` to keep track of the number of distinct integers in the current window for two different cases.
4. Iterate through the array using a right pointer `right`.
5. Update the counts and distinct counts for both cases as you expand the window.
6. While the number of distinct integers in the window exceeds `k`, contract the window by moving the left pointer(s) accordingly.
7. Calculate the number of subarrays that satisfy the condition using the difference between `left2` and `left1`.
8. Repeat until you reach the end of the array.

## Complexity
- Time complexity: O(n), where n is the length of the input array `nums`. We iterate through the array once.
- Space complexity: O(n), as we use two dictionaries to store the count of numbers in the window.

## Code
```python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left1, left2 = 0, 0
        count1, count2 = defaultdict(int), defaultdict(int)
        distinct1, distinct2 = 0, 0
        res = 0
        
        for right in range(n):
            if count1[nums[right]] == 0:
                distinct1 += 1
            count1[nums[right]] += 1
            
            if count2[nums[right]] == 0:
                distinct2 += 1
            count2[nums[right]] += 1
            
            while distinct1 > k:
                count1[nums[left1]] -= 1
                if count1[nums[left1]] == 0:
                    distinct1 -= 1
                left1 += 1
            
            while distinct2 > k - 1:
                count2[nums[left2]] -= 1
                if count2[nums[left2]] == 0:
                    distinct2 -= 1
                left2 += 1
                
            res += left2 - left1
        
        return res
```

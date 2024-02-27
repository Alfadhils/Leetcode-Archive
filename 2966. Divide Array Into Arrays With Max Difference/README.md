# 2966. Divide Array Into Arrays With Max Difference

## Intuition
To solve this problem, we need to divide the given array into subarrays such that the difference between the maximum and minimum elements in each subarray is less than or equal to a given threshold, k.

## Approach
1. Sort the array nums in non-decreasing order.
2. Iterate through the sorted array in steps of 3.
3. For each group of 3 consecutive elements, check if the difference between the maximum and minimum elements is greater than k.
4. If the difference is greater than k, return an empty list as it's not possible to create a valid subarray.
5. Otherwise, add the current group of 3 elements to the result list.
6. Return the result list containing subarrays.

## Complexity
- Time complexity: O(n log n) - Sorting the array takes O(n log n) time, where n is the size of the input array. The iteration through the sorted array takes linear time.
- Space complexity: O(n) - Additional space is used to store the sorted array and the result list.

## Code
``` python
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted((nums))
        n = len(nums)
        ans = []
        for i in range(0,n,3):
            subarray = nums[i:i+3]
            if subarray[-1] - subarray[0] > k:
                return []

            ans.append(nums[i:i+3])

        return ans
        
```
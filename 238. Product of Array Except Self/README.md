# 238. Product of Array Except Self

## Intuition
The problem asks to find the product of all elements in the array except the element itself. To solve this, we can multiply all the elements on the left side and all the elements on the right side of the current element to get the product of all elements except the current one.


## Approach
1. Compute the total product of all elements in the array.
2. Initialize an empty result array.
3. Iterate through each element in the array.
4. If the current element is zero, compute the product of elements on its left and right sides separately, excluding the zero element.
5. If the current element is not zero, divide the total product by the current element to get the product of all elements except the current one.
6. Append the result to the result array.
7. Return the result array.

## Complexity
- Time complexity: O(n)
  - We iterate through the array once to compute the total product, and then iterate through the array again to calculate the product of all elements except the current one.
- Space complexity: O(n)
  - We use an additional array of size n to store the result.

## Code
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def total_product(nums):
            product = 1
            for num in nums:
                product *= num
            return product

        n = len(nums)
        res = [0]*n
        product = total_product(nums)
        for i in range(n):
            if nums[i] == 0 :
                left = total_product(nums[0:i]) if nums[0:i] else 1
                right = total_product(nums[i+1:n+1]) if nums[i+1:n+1] else 1
                res[i] = left*right
            else :
                res[i] = product//nums[i]
        
        return res
```
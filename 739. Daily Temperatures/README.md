# 739. Daily Temperatures

## Intuition
The intuition behind this solution is to utilize a stack to keep track of the indices of temperatures that we haven't found the next warmer temperature for yet.

## Approach
1. Initialize an empty stack to store the indices of temperatures.
2. Initialize an array `ans` to store the result.
3. Iterate through the temperatures array.
4. For each temperature, check if the stack is empty. If it's empty, append the current index to the stack.
5. If the stack is not empty, compare the current temperature with the temperature at the index stored at the top of the stack.
6. While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack, pop the index from the stack and calculate the difference between the current index and the popped index (which represents the number of days until the next warmer temperature). Store this difference in the `ans` array at the popped index.
7. After the inner while loop, append the current index to the stack.
8. Return the `ans` array.

## Complexity
- Time complexity:
  - The time complexity of this solution is O(n), where n is the number of temperatures in the input array. Each temperature is processed exactly once in the worst case scenario.
- Space complexity:
  - The space complexity is also O(n) due to the stack and the `ans` array, both of which can potentially store up to n elements.

## Code
```
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n
        for i in range(n):
            if not stack:
                stack.append(i)
            else :
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    j = stack.pop()
                    ans[j] = i-j
                
                stack.append(i)

        return ans
```

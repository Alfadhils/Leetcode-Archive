# 412. Fizz Buzz
## Intuition
The problem involves iterating through numbers from 1 to n and replacing multiples of 3, 5, or both with "Fizz", "Buzz", or "FizzBuzz" accordingly. For other numbers, the integer itself is added to the result list.

## Approach
I use a simple loop to iterate through numbers from 1 to n. For each number, I check if it's a multiple of 15 (both 3 and 5), in which case I append "FizzBuzz" to the result list. If it's a multiple of 5, I append "Buzz". If it's a multiple of 3, I append "Fizz". Otherwise, I append the string representation of the number. The final result is a list of strings representing the FizzBuzz sequence for the given range.

## Complexity
- **Time complexity:** O(n) - The algorithm iterates through the numbers from 1 to n once, performing constant time operations for each iteration.
- **Space complexity:** O(n) - The space used is proportional to the input size since we store the FizzBuzz sequence in a list of length n.

## Code
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 5 == 0:
                res.append('Buzz')
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i))

        return res

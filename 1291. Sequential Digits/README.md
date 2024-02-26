# 1291. Sequential Digits

## Intuition
To generate all sequential digits between a given range, we can start from the digits 1 to 9 and iterate through each digit. For each starting digit, we incrementally append the next sequential digit until we reach the maximum limit specified by the high parameter. We then filter out the sequential digits that fall within the specified range.

## Approach
1. Initialize an empty list to store the sequential digits.
2. Iterate through digits from 1 to 9.
3. For each starting digit, initialize a variable to keep track of the current number.
4. Start appending the next sequential digit to the current number until either the current number exceeds the high limit or we reach the digit 9.
5. Check if the current number falls within the specified range. If it does, append it to the answer list.
6. Repeat steps 3-5 until all possible sequential digits are generated.
7. Return the sorted list of sequential digits.

## Complexity
- Time complexity:
    - Generating sequential digits involves iterating through digits from 1 to 9 and appending subsequent digits. This process has a complexity of O(1) since the maximum number of iterations is constant.
    - Sorting the answer list has a time complexity of O(n log n), where n is the number of sequential digits generated.
    - Overall, the time complexity is dominated by sorting and is O(n log n).
- Space complexity:
    - We use a list to store the sequential digits, which can grow up to O(n), where n is the number of sequential digits generated.
    - Hence, the space complexity is O(n).

## Code
```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        for i in range(1,10):
            curr = i
            next_seq = i+1

            while curr<=high and next_seq <=9:
                curr = curr*10 + next_seq
                if low <= curr <= high:
                    ans.append(curr)
                
                next_seq += 1
                
        return sorted(ans)
```

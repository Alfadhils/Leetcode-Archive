# 6. Zigzag Conversion

## Intuition

The problem involves converting a given string into a zigzag pattern based on a specified number of rows. My initial intuition is to iterate through the string and determine the appropriate row for each character based on the zigzag pattern.

## Approach

The approach is to simulate the zigzag pattern by creating a list of rows, where each row represents a row in the zigzag. We iterate through the string and append each character to the corresponding row in the zigzag pattern. The direction of movement (up or down) is controlled by a variable `step`. When we reach the top or bottom row, we change the direction accordingly. Finally, we concatenate the rows to obtain the zigzag conversion.

## Complexity

- Time complexity:

The time complexity of this solution is O(n), where n is the length of the input string. We iterate through the string once.

- Space complexity:

The space complexity is O(n), where n is the length of the input string. We store each character in the zigzag pattern in a list of rows.

## Code

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
```

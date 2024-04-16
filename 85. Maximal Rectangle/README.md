# 85. Maximal Rectangle

## Intuition
The problem involves finding the largest rectangular area of 1s in a binary matrix.

## Approach
The approach uses a stack to maintain the histogram of heights of 1s in each column. It iterates through each row of the matrix, updating the histogram and calculating the maximum area of rectangles formed.

## Complexity
- Time complexity: O(mn), where `m` is the number of rows and `n` is the number of columns in the matrix.
- Space complexity: O(n), where `n` is the number of columns in the matrix.

## Code
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        if rows==1 and cols==1:
            if matrix[0][0]=='1': 
                return 1
            else: 
                return 0

        h=[0]*(cols+1)
        maxArea=0

        for i, row  in enumerate(matrix):
            st=[-1] 
            row.append('0')
            for j, x in enumerate(row):
                if x=='1': 
                    h[j]+=1
                else: 
                    h[j]=0

                while len(st)>1 and (j==cols or h[j]<h[st[-1]]):
                    m=st[-1]
                    st.pop()
                    w=j-st[-1]-1
                    area=h[m]*w
                    maxArea=max(maxArea, area)

                st.append(j)

        return maxArea
```
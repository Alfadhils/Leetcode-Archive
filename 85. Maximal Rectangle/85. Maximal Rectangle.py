from typing import List

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
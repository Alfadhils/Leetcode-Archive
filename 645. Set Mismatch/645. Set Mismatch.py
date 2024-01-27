from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans1, ans2 = 0,0
        n = len(nums)
        snums = sorted(nums)
        for i,val in enumerate(snums):
            if i+1 < val:
                ans2 = i+1
                for j,val in enumerate(snums[i:]):
                    if j+i+2 == val:
                        ans1 = val
                break
            elif i+1 > val :
                ans1 = val
                for j,val in enumerate(snums[i:]):
                    if j+i != val:
                        ans2 = j+i
                        break
                    ans2 = j+i+1
                break

        return ans1, ans2
        
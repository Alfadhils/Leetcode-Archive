from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        j = 0
        for i in range(len(nums)):
            if i<1:
                res.append([nums[i]])
                continue

            if nums[i] == nums[i-1]:
                res[j].append(nums[i])
            else :
                res.append([nums[i]])
                j += 1
            
        output_list = []

        max_length = max(len(sublist) for sublist in res)
        for i in range(max_length):
            new_sublist = []
            for sublist in res:
                if i < len(sublist):
                    new_sublist.append(sublist[i])
            output_list.append(new_sublist)
        
        return output_list
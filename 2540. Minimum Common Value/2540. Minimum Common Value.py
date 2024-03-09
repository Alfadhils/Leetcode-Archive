from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1, idx2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while nums1[idx1] != nums2[idx2]:     
            if nums1[idx1] > nums2[idx2]:
                if idx2 >= n2 - 1:
                    return -1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                if idx1 >= n1 - 1:
                    return -1
                idx1 += 1
        
        return nums1[idx1]
        
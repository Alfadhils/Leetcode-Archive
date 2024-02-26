from typing import List

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
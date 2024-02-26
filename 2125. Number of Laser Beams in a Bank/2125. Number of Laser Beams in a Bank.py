from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank)<2:
            return 0

        total=0
        i=0
        while True:
            c = bank[i].count('1')
            while '1' not in bank[i+1]:
                if i+1 == len(bank)-1 :
                    break
                i+=1
            n = bank[i+1].count('1')
            total += c*n
            if i+1 == len(bank)-1 :
                break
            i+=1
        
        return total
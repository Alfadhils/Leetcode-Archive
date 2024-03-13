class Solution:
    def pivotInteger(self, n: int) -> int:
        if n <= 1:
            return n

        cumsum = 0
        cumsum_list = []
        for i in range(1,n+1):
            cumsum += i
            cumsum_list.append(cumsum)
        
        prev = 0
        for i in range(1,len(cumsum_list)):
            if cumsum_list[prev] + cumsum_list[i] == cumsum_list[-1]:
                return i+1
            
            prev = i

        return -1

        
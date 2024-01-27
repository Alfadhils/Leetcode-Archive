class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [0]*(k+1)
        dp[0] = 1

        for i in range(1,n):
            count = 0
            temp = []
            for j in range(k+1):
                count += dp[j]
                if j > i:
                    count -= dp[j-i-1]
                
                count %= mod
                temp.append(count)
            
            dp = temp
        
        return dp[k]
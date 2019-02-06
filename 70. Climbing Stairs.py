class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        dp=[]
        dp.append(1)
        dp.append(2)
        if n==1 or n==2:
            return n
        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]

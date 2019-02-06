class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> dp(n+3, 0);
        dp[1] = 1;
        dp[2] = 2;
        for(int i=3; i <=n; i++){
            dp[i] = dp[i-2] + dp[i-1];
        }
        return dp[n];
    }
};

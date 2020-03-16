class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        i = 0
        while i < n:
            if i == 0:
                dp.append(1)
            elif i == 1:
                dp.append(2)
            else:
                dp.append(dp[i-1] + dp[i-2])
            i += 1
        return dp[-1]


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.climbStairs(7)
    print(result)
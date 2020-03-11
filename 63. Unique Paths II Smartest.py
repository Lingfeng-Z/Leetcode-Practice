class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        dp = [[None for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        pass
                    elif i == 0 and j != 0:
                        dp[i][j] = dp[i][j-1]
                    elif j ==0 and i != 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(result)
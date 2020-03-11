class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        startpoint = [0, 0]
        endpoint = [len(obstacleGrid)-1, len(obstacleGrid[0])-1]
        return self.countPaths(obstacleGrid, startpoint, endpoint)
    
    def countPaths(self, matrix, start, end):
        if matrix[start[0]][start[1]] == 1 or matrix[end[0]][end[1]] == 1:
            return 0
        if start == end:
            return 1
        nextpoint1 = None
        nextpoint2 = None
        if start[0] < len(matrix)-1:
            if matrix[start[0]+1][start[1]] != 1:
                nextpoint1 = [start[0]+1, start[1]]
        if start[1] < len(matrix[0])-1:
            if matrix[start[0]][start[1]+1] != 1:
                nextpoint2 = [start[0], start[1]+1]
        if nextpoint1 is None and nextpoint2 is None:
            return 0
        elif nextpoint1 is None and nextpoint2 is not None:
            return self.countPaths(matrix, nextpoint2, end)
        elif nextpoint1 is not None and nextpoint2 is None:
            return self.countPaths(matrix, nextpoint1, end)
        else:
            return self.countPaths(matrix, nextpoint1, end)+self.countPaths(matrix, nextpoint2, end)

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.uniquePathsWithObstacles([[1]])
    print(result)
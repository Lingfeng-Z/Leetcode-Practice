class Solution:
    def minPathSum(self, grid: list) -> int:
        self.minSum = float("inf")
        start = [0, 0]
        self.end = [len(grid)-1, len(grid[0])-1]
        self.value = grid
        route = self.computeSum(start, 0)
        return self.minSum


    def computeSum(self, start, sum_now):
        sum_now += self.value[start[0]][start[1]]
        nextpoint1 = [start[0]+1, start[1]] if start[0] < len(self.value) -1 else None
        nextpoint2 = [start[0], start[1]+1] if start[1] < len(self.value[1]) -1 else None
        if nextpoint1 is None and nextpoint2 is None:
            if start == self.end:
                if sum_now < self.minSum:
                    self.minSum = sum_now
                return 1
            else:
                return 0
        elif nextpoint1 is None and nextpoint2 is not None:
            return self.computeSum(nextpoint2, sum_now)
        elif nextpoint1 is not None and nextpoint2 is None:
            return self.computeSum(nextpoint1, sum_now)
        else:
            return self.computeSum(nextpoint1, sum_now) + self.computeSum(nextpoint2, sum_now)

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
    print(result)
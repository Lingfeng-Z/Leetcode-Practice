class Solution:
    def minPathSum(self, grid: list) -> int:
        self.start = tuple([0,0])
        self.end = tuple([len(grid)-1, len(grid[0])-1])
        self.connect = {}
        self.visit = {}
        self.value = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.visit[tuple([i, j])] = False
                if i != len(grid)-1:
                    self.connect[tuple([i, j])] = [tuple([i+1, j])]
                if j != len(grid[0])-1:
                    if tuple([i,j]) in self.connect.keys():
                        self.connect[tuple([i, j])].append(tuple([i, j+1]))
                    else:
                        self.connect[tuple([i, j])] = [tuple([i, j+1])]
                if i == len(grid)-1 and j == len(grid[0])-1:
                    self.connect[tuple([i, j])] = []
        return self.DFS()

    def DFS(self):
        stack = [self.start]
        sum = self.value[0][0]
        min_sum = float("inf")
        while len(stack) != 0:
            neighbour_stat = [self.visit[i] for i in self.connect[stack[-1]]]
            if False in neighbour_stat:
                i = neighbour_stat.index(False)
                stack.append(self.connect[stack[-1]][i])
                sum += self.value[stack[-1][0]][stack[-1][1]]
                self.visit[stack[-1]] = True
            else:
                if self.end in stack:
                    if sum < min_sum:
                        min_sum = sum
                past_point = stack.pop(-1)
                sum -= self.value[past_point[0]][past_point[1]]
                for j in self.connect[past_point]:
                    self.visit[j] = False
        return min_sum


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]])
    print(result)
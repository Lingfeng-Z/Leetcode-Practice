
class Map:
    def __init__(self):
        self.connect = {}
        self.visit_status = {}
        self.map_effectiveness = True
    
    def makeMap(self, matrix: list):
        col_num = len(matrix[0])
        row_num = len(matrix)
        self.start = tuple([0,0])
        self.end = tuple([row_num - 1, col_num - 1])
        for m in range(row_num):
            for n in range(col_num):
                if matrix[m][n] == 1:
                    if tuple([m,n]) == self.start or tuple([m,n]) == self.end:
                        self.map_effectiveness = False
                    continue
                elif m == row_num -1 and n != col_num -1:
                    if matrix[m][n+1] == 1:
                        self.connect[tuple([m,n])] = []
                    else:
                        self.connect[tuple([m,n])] = [tuple([m, n + 1])]
                elif n == col_num -1 and m != row_num -1:
                    if matrix[m+1][n] == 1:
                        self.connect[tuple([m,n])] = []
                    else:
                        self.connect[tuple([m,n])] = [tuple([m + 1, n])]
                elif m == row_num -1 and n == col_num -1:
                    self.connect[tuple([m,n])] = []
                else:
                    flag_right = True
                    flag_down = True
                    if matrix[m][n+1] == 1:
                        flag_right = False
                    if matrix[m+1][n] == 1:
                        flag_down = False
                    if flag_right != False:
                        self.connect[tuple([m,n])] = [tuple([m, n + 1])]
                    if flag_down != False:
                        if tuple([m,n]) in self.connect.keys():
                            self.connect[tuple([m,n])].append(tuple([m + 1, n]))
                        else:
                            self.connect[tuple([m,n])] = [tuple([m + 1,n])]
                    if flag_right == False and flag_down == False:
                        self.connect[tuple([m,n])] = []
                self.visit_status[tuple([m,n])] = False
        self.visit_status[self.start] = True
        


#无向图的方法
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        map = Map()
        map.makeMap(obstacleGrid)
        if map.map_effectiveness == False:
            return 0
        else:
            return self.DFS(map)

    def DFS(self, map: Map):
        if map.start == map.end:
            return 1
        stack = [map.start]
        count = 0
        while len(stack) != 0:
            current_point = stack[-1]
            neighbour_visit = [map.visit_status[i] for i in map.connect[current_point]]
            if False in neighbour_visit:
                i = neighbour_visit.index(False)
                stack.append(map.connect[current_point][i])
                map.visit_status[map.connect[current_point][i]] = True
            else:
                if map.end in stack:
                    count += 1
                last_point = stack.pop(-1)
                for l in map.connect[last_point]:
                    map.visit_status[l] = False
        return count
'''                          

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        postion = m + n - 2
        need_to_fill = n - 1
        warning = 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    if (i == 0 and j == 0) or (i == n-1 and j == m-1):
                        return 0
                    else:
                        parent_point = []
                        if i-1 >= 0:
                            parent_point.append([i-1,j])
                            postion -= 1
                        if j-1 >= 0:
                            parent_point.append([i, j-1])
                            postion -= 1
                            need_to_fill -= 1
                        if parent_point == [[0,0]]:
                            warning += 1
                            if warning == 2:
                                return 0
        if need_to_fill == 0 or postion == 0:
            return 0
        else:
            P_numerator = 1
            P_denominator = 1
            for i in range(1, need_to_fill+1):
                P_numerator = P_numerator * postion
                postion -= 1
                P_denominator = P_denominator * i
                return int(P_numerator / P_denominator)
'''

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.uniquePathsWithObstacles([[0,0,1], [0,0,0], [0,0,0]])
    print(result)
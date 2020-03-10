class Solution:
    def generateMatrix(self, n: int) -> list:
        self.matrix = [[None for i in range(n)] for j in range(n)]
        self.fillNum(n)
        return self.matrix
    
    def fillNum(self, n: int):
        loop_time = 1
        flag_x = 1
        flag_y = 1
        x_limit = n-1
        x_min = 0
        y_limit = n-1
        y_min = 0
        currentcoordinate = [x_min, y_min]
        startpoint = currentcoordinate.copy()
        while True:
            self.matrix[currentcoordinate[0]][currentcoordinate[1]] = loop_time
            loop_time += 1
            if loop_time == n ** 2 + 1:
                break
            if (currentcoordinate[0] == x_min and currentcoordinate[1] != y_limit) or (currentcoordinate[0] == x_limit and currentcoordinate[1] != y_min):
                currentcoordinate[1] += flag_y * 1
                if currentcoordinate[1] == y_limit:
                    flag_y = -1 * flag_y
                continue
            if (currentcoordinate[1] == y_min and currentcoordinate[0] != x_min) or (currentcoordinate[1] == y_limit and currentcoordinate[0] != x_limit):
                if currentcoordinate == [startpoint[0] + 1, startpoint[1]]:
                    x_limit -= 1
                    y_limit -= 1
                    x_min += 1
                    y_min += 1
                    flag_x = 1
                    flag_y = 1
                    currentcoordinate = [x_min, y_min]
                    startpoint = currentcoordinate.copy()
                else:
                    currentcoordinate[0] += flag_x * 1
                    if currentcoordinate[0] == x_limit:
                        flag_x = -1 * flag_x
            



if __name__ == "__main__":
    Solu = Solution()
    result = Solu.generateMatrix(5)
    print(result)
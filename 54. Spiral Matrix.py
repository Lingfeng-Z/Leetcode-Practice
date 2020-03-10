class Solution:
    def spiralOrder(self, matrix: list):
        m = len(matrix)
        if m != 0:
            n = len(matrix[0])
        else:
            return []
        limit = [[m-1, n-1], [1, 0]]
        flag = 1
        if m == 1 or n == 1:
            if m != 1:
                return [matrix[i][0] for i in range(m)]
            elif n != 1:
                return [matrix[0][i] for i in range(n)]
            else:
                return [matrix[0][0]]
        address = [0,0]
        result = [matrix[address[0]][address[1]]]
        for i in range(2):
            for j in range(1,-1,-1):
                if address[j] == limit[i][j]:
                        break
                while True:
                    address[j] += flag * 1
                    result.append(matrix[address[0]][address[1]])
                    if address[j] == limit[i][j]:
                        break
            flag = flag * -1
        if m == 2 or n  == 2:
            return result
        else:
            result.extend(self.spiralOrder([[matrix[x][y] for y in range(1, n-1)] for x in range(1, m-1)]))
            return result


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
    print(result)
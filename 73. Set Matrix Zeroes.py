import copy


class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in row:
            matrix[i] = [0 for k in range(len(matrix[0]))]
        for j in col:
            for o in range(len(matrix)):
                matrix[o][j] = 0
        print(matrix)


if __name__ == "__main__":
    Solu = Solution()
    Solu.setZeroes([[1,1,1],[1,0,1],[1,1,1]])

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)-1):
            if target >= matrix[i][0] and target < matrix[i+1][0]:
                if target in matrix[i]:
                    return True
                else:
                    return False
        if target in matrix[-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.searchMatrix([[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 50)
    print(result)
class Solution:
    def solveSudoku(self, board: list):
        row = {}
        col = {}
        matrix = {}
        point_set = []
        for i in range(9):
            row[i] = {}
            col[i] = {}
            matrix[i] = {}
            for j in range(1, 10):
                row[i][j] = False
                col[i][j] = False
                matrix[i][j] = False
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i][int(board[i][j])] = True
                    col[j][int(board[i][j])] = True
                    matrix[int(i/3)*3+int(j/3)][int(board[i][j])] = True
                else:
                    point_set.append([i,j])
        stack = []
        for i in point_set:
            
        


if __name__ == "__main__":
    s = Solution()
    s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

    

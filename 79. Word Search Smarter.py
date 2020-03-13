import copy

class Solution:
    def exist(self, board: list, word: str) -> bool:
        position = []
        self.connect = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = None
                    if self.checkOut([i,j], new_board, word[1:]) == 1:
                        return True
        return False
    
    def checkOut(self, head, matrix, remaining):
        direction = [[-1,0], [+1,0], [0,-1], [0,+1]]
        if len(remaining) == 0:
            return 1
        else:
            temp = []
            for i in direction:
                if (head[0]+i[0]) >=0 and (head[0]+i[0]) < len(matrix) and (head[1]+i[1]) >=0 and (head[1]+i[1]) < len(matrix[0]):
                    if matrix[head[0]+i[0]][head[1]+i[1]] == remaining[0]:
                        temp.append([head[0]+i[0], head[1]+i[1]])
            if len(temp) == 0:
                return 0
            else:
                for j in temp:
                    new_matrix = copy.deepcopy(matrix)
                    new_matrix[j[0]][j[1]] = None
                    if self.checkOut(j, new_matrix, remaining[1:]) == 1:
                        return 1
                return 0


if __name__ == "__main__":
    Solu = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    result = Solu.exist(board, word)
    print(result)
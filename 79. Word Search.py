import copy

class Solution:
    def exist(self, board: list, word: str) -> bool:
        position = []
        self.connect = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    position.append(tuple([i,j]))
                self.connect[tuple([i, j])] = []
                if i < len(board)-1:
                    self.connect[tuple([i,j])] = [tuple([i+1,j])]
                if i > 0:
                    if tuple([i,j]) not in self.connect.keys():
                        self.connect[tuple([i,j])] = [tuple([i-1, j])]
                    else:
                        self.connect[tuple([i,j])].append(tuple([i-1, j]))
                if j > 0:
                    self.connect[tuple([i,j])].append(tuple([i, j-1]))
                if j < len(board[0])-1:
                    self.connect[tuple([i,j])].append(tuple([i, j+1]))     
        for k in position:
            history_points = []
            history_points.append(k) 
            if self.checkOut(k, board, word[1:], history_points) == 1:
                return True
        return False
    
    def checkOut(self, head, matrix, remaining, his):
        if len(remaining) == 0:
            return 1
        else:
            temp = [i for i in self.connect[head] if matrix[i[0]][i[1]] == remaining[0] and i not in his]
            if len(temp) == 0:
                return 0
            else:
                for j in temp:
                    new_history_points = copy.deepcopy(his)
                    new_history_points.append(j)
                    if self.checkOut(j, matrix, remaining[1:], new_history_points) == 1:
                        return 1
                return 0


if __name__ == "__main__":
    Solu = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    result = Solu.exist(board, word)
    print(result)
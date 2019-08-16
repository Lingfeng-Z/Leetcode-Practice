class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dict_candidate = {}
        dict_affect = {}
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == '.':
                    candidate_set, affect_address = self.findCandidate(i, j, board)
                    name = tuple([i,j])
                    dict_candidate[name] = candidate_set
                    dict_affect[name] = affect_address
                j += 1
            i += 1
        '''
        min_candidate = 9
        for k in dict_candidate.keys():
            if min_candidate > len(dict_candidate[k]):
                min_candidate = len(dict_candidate[k])
        if min_candidate == 1:
            while 1:
                flag = 0
                for k in dict_candidate.keys():
                    m = k[0]
                    n = k[1]
                    if len(dict_candidate[k]) >0:
                        flag =1
                    if len(dict_candidate[k]) == 1:
                        board[m][n] = dict_candidate[k][0]
                        dict_candidate[k].pop()
                        dict_candidate, dict_affect = self.modiCandidate(dict_candidate, dict_affect, m, n, board)
                if flag == 0 :
                    break
        else:
        '''
        new_board = board
        new_dict_candidate = dict_candidate
        new_dict_affect = dict_affect
        min_candidate, address = self.findMin(new_dict_candidate)
        flag = 0
        while flag == 0:
            for candidate in new_dict_candidate[address]:
                new_board[address[0], address[1]] = candidate
                new_dict_candidate.remove(candidate)
                new_dict_candidate, new_dict_affect = self.modiCandidate(new_dict_candidate, new_dict_affect, address[0], address[1], board)

            if min_candidate == 0:
                flag =1

    def findCandidate(self, i, j, board):
        full = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        appearance = []
        affect = []
        m = 0
        while m < 9:
            if board[i][m] != '.':
                appearance.append(board[i][m])
            else:
                affect.append([i, m])
            if board[m][j] != '.':
                appearance.append(board[m][j])
            else:
                affect.append([m, j])
            m += 1
        if i < 3:
            limit_x = 3
        elif i < 6:
            limit_x = 6
        else:
            limit_x = 9
        if j < 3:
            limit_y = 3
        elif j < 6:
            limit_y = 6
        else:
            limit_y = 9
        m = limit_x - 3
        while m < limit_x:
            n = limit_y - 3
            while n < limit_y:
                if board[m][n] != '.':
                    appearance.append(board[m][n])
                else:
                    affect.append([m, n])
                n += 1
            m += 1
        appearance = list(set(appearance))
        affect = list(set([tuple(x) for x in affect]))
        affect = [list(x) for x in affect]
        candidate = full - set(appearance)
        return list(candidate), affect

    def modiCandidate(self, dict_candidate, dict_affect, m, n, board):
        for a in dict_affect.keys():
            if [m,n] in dict_affect[a]:
                dict_affect[a].remove([m, n])
                if board[m][n] in dict_candidate[a]:
                    dict_candidate[a].remove(board[m][n])
        return dict_candidate, dict_affect

    def findMin(self, dict_1):
        min_candidate = 9
        address = (0, 0)
        flag = 0
        for k in dict_1.keys():
            if min_candidate > len(dict_1[k]) and len(dict_1[k]) != 0:
                flag = 1
                min_candidate = len(dict_1[k])
                address = k
        if flag == 0:
            min_candidate = 0
        return min_candidate, address

    def 

if __name__ == "__main__":
    s = Solution()
    s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        i = 0
        while i < 9:
            k = 0
            j = 0
            while j < 9:
                if board[i][j] == '.':
                    k += 1
                j += 1
            if len(list(set(board[i]))) != 10 - k:
                return False
            i += 1
        i = 0
        while i < 9:
            s = []
            k = 0
            j = 0
            while j < 9:
                s.append(board[j][i])
                if board[j][i] == '.':
                    k += 1
                j += 1
            if len(list(set(s))) != 10 - k:
                return False
            i += 1
        m = 3
        while m < 10:
            n =3
            while n < 10:
                i = m-3
                s = []
                k = 0
                while i < m:
                    j = n-3
                    while j < n:
                        s.append(board[i][j])
                        if board[i][j] == '.':
                            k += 1
                        j += 1
                    i += 1
                if len(list(set(s))) != 10 - k:
                    return False
                n += 3
            m += 3
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku())
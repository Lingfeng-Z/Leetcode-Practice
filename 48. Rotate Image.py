#Faster than 96.60%, very good algorithm
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix) - 1
        m = 0
        result = []
        while m < int((len(matrix)+1)/2):
            i = m
            while i < len(matrix) - 1 - m:
                result.append([[m, i]] + self.findNextseries([m, i], [m, i], dim))
                i += 1
            m += 1
        print(result)
        for r in result:
            u = 0
            temp1 = matrix[r[0][0]][r[0][1]]
            while u < len(r):
                temp2 = matrix[r[u][0]][r[u][1]]
                if u == 0:
                    matrix[r[u][0]][r[u][1]] = matrix[r[-1][0]][r[-1][1]]
                else:
                    matrix[r[u][0]][r[u][1]] = temp1
                    temp1 = temp2
                u += 1
        print(matrix)


    def findNextseries(self, start, now, dim):
        series = []
        nexp = [now[1], dim - now[0]]
        if nexp != start:
            series.append(nexp)
            now = nexp
            temp = self.findNextseries(start, now, dim)
            series = series + temp
            return series
        else:
            return series



if __name__ == '__main__':
    s = Solution()
    testcase = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s.rotate(testcase)
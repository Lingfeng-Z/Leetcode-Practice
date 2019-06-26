class Solution(object):
    def edit_distance(self, string1, string2):
        if len(string1) == 0:
            return len(string2)
        elif len(string2) == 0:
            return len(string1)
        else:
            if string1[-1] == string2[-1]:
                flag = 0
            else:
                flag = 1
            distance1 = self.edit_distance(string1[:-1], string2) + 1
            distance2 = self.edit_distance(string1, string2[:-1]) + 1
            distance3 = self.edit_distance(string1[:-1], string2[:-1]) + flag
            return min(distance1, distance2, distance3)

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.edit_distance(word1, word2)

class Solution2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        matrix = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]
        for j in range(len1 + 1):
            matrix[0][j] = j
        for i in range(len2 + 1):
            matrix[i][0] = i
        for i in range(len2):
            for j in range(len1):
                if word2[i] == word1[j]:
                    flag = 0
                else:
                    flag = 1
                matrix[i + 1][j + 1] = min(matrix[i][j + 1] + 1, matrix[i + 1][j] + 1,
                                           matrix[i][j] + flag)
        return matrix[len2][len1]


if __name__ == "__main__":
    sol = Solution2()
    print(sol.minDistance("prosperity","properties"))
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 0
        game = '1'
        while i < n - 1:
            answer = ''
            j = 0
            count = 1
            while j < len(game):
                if j < len(game) - 1 or count != 1:
                    if j == len(game) - 1:
                        answer = answer + str(count) + game[j]
                        count = 1
                        j += 1
                        continue
                    elif game[j] == game[j + 1]:
                        count += 1
                        j += 1
                        continue
                    elif game[j] != game[j + 1] and count > 1:
                        answer = answer + str(count) + game[j]
                        count = 1
                        j += 1
                        continue
                    else:
                        answer = answer + self.searchDict(game[j])
                        j += 1
                        continue
                else:
                    answer = answer + self.searchDict(game[j])
                    j += 1
                    continue
            game = answer
            i += 1
        return game

    def searchDict(self, str):
        return '1' + str

if __name__ == '__main__':
    s = Solution()
    result = s.countAndSay(int(input()))
    print(result)
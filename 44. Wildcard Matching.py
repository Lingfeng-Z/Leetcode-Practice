class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        flag = False
        len_p = len(p)
        i = 0
        j = 0
        while i < len_p:
            if j == len(s) and self.StringClassification(p[i:]):
                return flag
            elif p[i] == '*':
                while 1:
                    if i + 1 == len_p:
                        flag = True
                        return flag
                    elif p[i+1] == '*':
                        i += 1
                    elif p[i+1] == '?':
                        p[i + 1] == '*'
                        i += 1
                        j += 1
                        if j > len(s):
                            return flag
                    else:
                        break
                position = self.findPosition(s, p[i + 1 ])
                candidate_temp = [s[l:] for l in position if l >= j]
                for dex, k in enumerate(candidate_temp):
                    j = position[dex]
                    flag = self.isMatch(k, p[i + 1:])
                    if flag == True:
                        return flag
                return flag
            elif p[i] == '?':
                i += 1
                j += 1
                continue
            else:
                if s[i] == p[i]:
                    i += 1
                    j += 1
                    continue
                else:
                    return flag
        if j == len(s):
            flag = True
        return flag

    def StringClassification(self, s: str) -> bool:
        if "*" not in s:
            return True
        else:
            classification_result = [True for i in s if i == "*"]
            if len(classification_result) == len(s):
                return False
            else:
                return True

    def findPosition(self, s: str, p: str) -> list:
        target = p[0]
        position = []
        i = 0
        while i < len(s):
            if s[i] == target:
                position.append(i)
            i += 1
        return position

if __name__ == '__main__':
    Solve = Solution()
    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    print(Solve.isMatch(s, p))
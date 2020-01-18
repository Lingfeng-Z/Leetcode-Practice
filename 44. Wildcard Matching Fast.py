import time

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch(s, p, 1)

    def _isMatch(self, s: str, p: str, flag1) -> bool:
        if flag1 == 1:
            while 1:
                if "**" in p or "*?" in p:
                    p = p.replace("**", "*")
                    p = p.replace("*?", "?*")
                else:
                    break
        flag = False
        len_p = len(p)
        i = 0
        j = 0
        while i < len_p:
            if p[i] == "*":
                if i+1 == len_p:
                    flag = True
                    return flag
                else:
                    str_temp = ""
                    for _ in p[i+1:]:
                        if _ != '*' and _ != '?':
                            str_temp += _
                        else:
                            break
                    i += len(str_temp)
                    position = self.findPosition(s, str_temp)
                    if position == []:
                        return flag
                    else:
                        candidate_temp = [s[l:] for l in position if l >= j+len(str_temp)]
                        for dex, k in enumerate(candidate_temp):
                            flag = self._isMatch(k, p[i+1:], 0)
                            if flag == True:
                                return flag
                        return flag
            elif p[i] == "?":
                if i >= len(s):
                    return flag
                else:
                    i += 1
                    j += 1
                    continue
            else:
                if i >= len(s):
                    return flag
                elif s[i] == p[i]:
                    i += 1
                    j += 1
                    continue
                else:
                    return flag
        if j == len(s):
            flag = True
        return flag

    def findPosition(self, s: str, p: str) -> list:
        position = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == p[i]:
                i += 1
                j += 1
            else:
                j = j-i+1
                i = 0
            if i == len(p):
                position.append(j)
                j = j-i+1
                i = 0
        return position




if __name__ == '__main__':
    start = time.time()
    Solve = Solution()
    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    print(Solve.isMatch(s, p))
    end = time.time()
    print("Cost time {:.2f}".format(end - start))
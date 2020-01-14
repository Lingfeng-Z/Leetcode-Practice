class Solution:
    def isMatchPartial(self, s: str, p: str) -> bool:
        flag = False
        if p == '*' or p == '?':
            flag = True
            return flag
        elif len(p) == 1:
            i = 0
            while i < len(s):
                if s[i] == p[0]:
                    flag = True
                    return flag
                i += 1
        elif len(p) > len(s):
            return flag
        else:
            candidate_string = []
            i = 0
            while i < len(s):
                if s[i] == p[0]:
                    candidate_string.append(s[i:])
                i += 1
            for i in candidate_string:
                flag = self.chatMatch(i, p[1:])
                if flag == True:
                    return flag

    def charMatch(self, s: str, p: str) -> bool:
        flag = False
        len_p = len(p)
        i = 0
        while i < len_p:
            if p[i] == '*':
                position = self.findPosition(s, p[i + 1])
                candidate_temp = []
                for j in position:
                    candidate_temp.append(s[j:])
                for k in candidate_temp:
                    flag = self.charMatch(k, p[i + 1:])
                    if flag == True:
                        break
            elif p[i] == '?':
                i += 1
                continue
            else:
                if s[i] == p[i]:
                    i += 1
                    continue
                else:
                    return flag
        flag = True
        return flag

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
    s = "aa"
    p = "a"
    print(Solve.isMatchPartial(s, p))